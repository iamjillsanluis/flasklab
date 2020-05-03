from datetime import datetime
from typing import List

from flask import Flask, abort, request
from flask.views import MethodView

from pydantic import BaseModel


app = Flask(__name__)


class Identity(BaseModel):
    guid: str
    name: str
    created_at: datetime


class IdentityList(BaseModel):
    identities: List[Identity]


class IdentityRepository(object):
    def __init__(self):
        seed = [
            Identity(guid="1000-a", name="Homer Simpson", created_at=datetime.now()),
            Identity(guid="1000-b", name="Marge Simpson", created_at=datetime.now()),
            Identity(guid="1000-c", name="Bart Simpson", created_at=datetime.now()),
            Identity(guid="1000-d", name="Lisa Simpson", created_at=datetime.now()),
            Identity(guid="1000-e", name="Maggie Simpson", created_at=datetime.now()),
        ]
        self._cache = { x.guid: x for x in seed }

    def add(self, identity):
        if identity.guid not in self._cache:
            self._cache[identity.guid] = identity
        else:
            raise Exception(f"Record with guid: {identity.guid} already exists.")

    def get(self, identity_guid):
        return self._cache.get(identity_guid)

    def all(self):
        return self._cache.values()


identity_repository = IdentityRepository()


class IdentityApi(MethodView):
    def get(self, identity_guid):
        identity = identity_repository.get(identity_guid)

        if identity:
            return identity.json()
        else:
            abort(404)


class IdentitiesApi(MethodView):
    def post(self):
        identity = Identity(**request.json)
        identity_repository.add(identity)
        return identity.json()

    def get(self):
        return IdentityList(identities=list(identity_repository.all())).json()


app.add_url_rule("/identities/<identity_guid>", view_func=IdentityApi.as_view("identity"))
app.add_url_rule("/identities", view_func=IdentitiesApi.as_view("identities"))

app.run()
