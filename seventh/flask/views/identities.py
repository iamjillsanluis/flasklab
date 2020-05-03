from typing import List

from flask import request, abort
from flask.views import MethodView
from pydantic import BaseModel

from seventh.identities.models import Identity
from seventh.identities.repositories import IdentityRepository


class IdentityList(BaseModel):
    identities: List[Identity]


# TODO: Fix this! This is dirty.
#   At this point API only has one dependency, the repository instance.
#   But over time, it is not far fetched for APIs to depend on many collaborators.
#   If we don't create/wire these dependencies, it could lead to tricky bugs to
#   debug.
#   For now, I will keep as is and refactor later.
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
