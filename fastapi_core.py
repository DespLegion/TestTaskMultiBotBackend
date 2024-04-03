from fastapi import FastAPI

from djangoORM import settings
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from core.bot_users.endpoints import user_router
from core.weather.endpoints import weather_router
from core.to_do_list.endpoints import to_do_list_router
from core.testing.endpoints import testing_router
from core.photo_editing.endpoints import photo_edit_router
from fastapi_utils.auth import BackendAuth


backauth = BackendAuth()
service_router = APIRouter(dependencies=[Depends(backauth)])


@service_router.get("/status")
def ping_backend():
    return JSONResponse(status_code=200, content={"status": "success", "message": True})


description = """
TG Multi Bot Backend API
"""

app = FastAPI(
    title="TG Multi Bot Test Task",
    description=description,
    openapi_url=f"/api/openapi.json",
    version="0.0.1",
    debug=settings.DEBUG,
)


app.include_router(user_router, tags=["User"], prefix="/api")
app.include_router(weather_router, tags=["Weather"], prefix="/api")
app.include_router(to_do_list_router, tags=["TO-DO"], prefix="/api")
app.include_router(testing_router, tags=["Testing"], prefix="/api")
app.include_router(photo_edit_router, tags=["Edit Photo"], prefix="/api")
app.include_router(service_router, tags=["Service"], prefix="/api")
