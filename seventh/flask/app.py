from flask import Flask

from seventh.flask.views.hooks import HooksApi
from seventh.identities.repositories import IdentityRepository


def create_app():
    app = Flask(__name__)

    from seventh.flask.views.identities import IdentitiesApi, IdentityApi

    identity_repository = IdentityRepository()

    app.add_url_rule(
        "/identities/<identity_guid>",
        view_func=IdentityApi.as_view(
            "identity", identity_repository=identity_repository
        ),
    )
    app.add_url_rule(
        "/identities",
        view_func=IdentitiesApi.as_view(
            "identities", identity_repository=identity_repository
        ),
    )
    app.add_url_rule(
        "/hooks/<hook_guid>",
        view_func=HooksApi.as_view("hooks"),
    )

    return app
