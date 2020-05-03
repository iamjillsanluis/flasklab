from datetime import datetime

from pydantic import BaseModel


class Identity(BaseModel):
    guid: str
    name: str
    created_at: datetime
