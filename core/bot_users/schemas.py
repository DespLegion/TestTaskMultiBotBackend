from pydantic import BaseModel
from typing import Optional


class BotUserSch(BaseModel):
    user_id: int
    user_username: Optional[str]
    user_firstname: str
    user_lastname: Optional[str]


class BotUserCrResponse(BaseModel):
    status: str
    message: str


class BotUserResponse(BaseModel):
    status: str
    user: BotUserSch
