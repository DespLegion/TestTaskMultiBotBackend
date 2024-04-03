from django.core.files.images import ImageFile
from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse

from fastapi_utils.auth import BackendAuth
from core.bot_users.models import BotUser
from .models import WatermarkModel
from .schemas import WatermarkUpdateResp


backauth = BackendAuth()
photo_edit_router = APIRouter(dependencies=[Depends(backauth)])


@photo_edit_router.get("/watermark/{user_id}")
def get_watermark(user_id: int):
    if not BotUser.objects.filter(user_id=user_id).exists():
        return JSONResponse(status_code=400, content={"status": "error", "message": "No user with that ID exists"})

    try:
        user_watermark = WatermarkModel.objects.get(user__user_id=user_id)

        return FileResponse(status_code=200, path=f"{user_watermark.watermark_img}")
    except Exception as err:
        return JSONResponse(status_code=500, content={"status": "error", "message": f"Error: {err}"})


@photo_edit_router.patch("/watermark/{user_id}", response_model=WatermarkUpdateResp)
def update_watermark(user_id: int, watermark_img: UploadFile = File(...)):
    if not BotUser.objects.filter(user_id=user_id).exists():
        return JSONResponse(status_code=400, content={"status": "error", "message": "No user with that ID exists"})

    try:
        img2 = ImageFile(watermark_img.file)

        user_watermark = WatermarkModel.objects.get(user__user_id=user_id)

        user_watermark.watermark_img.save(f"{watermark_img.filename}.png", img2)
        user_watermark.save()
        return JSONResponse(status_code=200, content={"status": "success", "message": "Watermark updated successfully"})
    except Exception as err:
        return JSONResponse(status_code=500, content={"status": "error", "message": f"Error: {err}"})
