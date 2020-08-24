

import logging

from flask.views import MethodView
from pydantic import BaseModel

from seventh.flask.formatters import response_json

log = logging.getLogger(__name__)


def get_decorator(target):
    def decorator(*args, **kwargs):
        kwargs["hook_guid"] = f"GET_{kwargs['hook_guid']}"
        return target(*args, **kwargs)

    return decorator


def scoped(scope):
    def custom_wrapper(target):
        def decorator(*args, **kwargs):
            kwargs["hook_guid"] = f"{scope}_{kwargs['hook_guid']}"
            return target(*args, **kwargs)

        return decorator
    return custom_wrapper


class Hook(BaseModel):
    guid: str
    target: str


class HooksApi(MethodView):
    decorators = [response_json]

    @scoped(scope="GET_x_")
    def get(self, hook_guid):
        return Hook(guid=hook_guid, target="GET")

    @scoped(scope="DELETE_x_")
    def delete(self, hook_guid):
        return Hook(guid=hook_guid, target="DELETE")

