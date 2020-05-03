from flask import Flask


def create_app():
    app = Flask(__name__)

    from seventh.flask.views.identities import IdentitiesApi, IdentityApi

    app.add_url_rule(
        "/identities/<identity_guid>", view_func=IdentityApi.as_view("identity")
    )
    app.add_url_rule("/identities", view_func=IdentitiesApi.as_view("identities"))

    return app
