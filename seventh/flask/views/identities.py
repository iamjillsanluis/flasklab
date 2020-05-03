from typing import List

from flask import request, abort
from flask.views import MethodView
from pydantic import BaseModel

from seventh.flask.formatters import response_json
from seventh.identities.models import Identity


class IdentityList(BaseModel):
    identities: List[Identity]


class IdentityApi(MethodView):
    decorators = [response_json]

    def __init__(self, identity_repository):
        self._identity_repository = identity_repository

    def get(self, identity_guid):
        identity = self._identity_repository.get(identity_guid)

        if identity:
            return identity
        else:
            abort(404)


class IdentitiesApi(MethodView):
    decorators = [response_json]

    def __init__(self, identity_repository):
        self._identity_repository = identity_repository

    def post(self) -> BaseModel:
        identity = Identity(**request.json)
        self._identity_repository.add(identity)
        return identity

    def get(self) -> BaseModel:
        return IdentityList(identities=list(self._identity_repository.all()))
