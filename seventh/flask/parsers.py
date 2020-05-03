from flask import request
from pydantic import BaseModel


def request_as(model: BaseModel.__class__):
    return model(**request.json)
