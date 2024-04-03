from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from .models import BotUser
from core.photo_editing.models import WatermarkModel
from .schemas import BotUserSch, BotUserResponse, BotUserCrResponse
from fastapi_utils.auth import BackendAuth

from datetime import datetime


backauth = BackendAuth()
user_router = APIRouter(dependencies=[Depends(backauth)])


@user_router.get("/user/e/{user_id}")
def bot_user_exists(user_id: int):
    if not BotUser.objects.filter(user_id=user_id).exists():
        return JSONResponse(status_code=200, content={"status": "success", "user_exists": False})
    return JSONResponse(status_code=200, content={"status": "success", "user_exists": True})


@user_router.get("/user/{user_id}", response_model=BotUserResponse)
def get_bot_user(user_id: int):
    if not BotUser.objects.filter(user_id=user_id).exists():
        return JSONResponse(status_code=400, content={"status": "error", "error": "No user with that ID exists"})

    user = BotUser.objects.get(user_id=user_id)
    formar_user_date = datetime.strftime(user.user_add_date, "%Y.%m.%d %H:%M")
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "user": {
                "user_id": user.user_id,
                "user_username": user.user_username,
                "user_firstname": user.user_firstname,
                "user_lastname": user.user_lastname,
                "user_add_date": formar_user_date,
            }
        }
    )


@user_router.post("/user", response_model=BotUserCrResponse)
def create_user(user: BotUserSch):
    if BotUser.objects.filter(user_id=user.user_id).exists():
        return JSONResponse(status_code=400, content={"status": "error", "message": "User with this ID already exists"})
    try:
        new_user = BotUser()
        new_user.user_id = int(user.user_id)
        new_user.user_username = user.user_username
        new_user.user_firstname = user.user_firstname
        new_user.user_lastname = user.user_lastname
        new_user.save()
        new_watermark = WatermarkModel()
        new_watermark.user = new_user
        new_watermark.save()
        return JSONResponse(status_code=200, content={"status": "success", "message": "New user successfully added"})
    except Exception as err:
        return JSONResponse(status_code=500, content={"status": "error", "message": f"{err}"})
