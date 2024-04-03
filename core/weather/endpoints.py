from fastapi import APIRouter, Depends
from fastapi_utils.auth import BackendAuth
from fastapi.responses import JSONResponse
from core.bot_users.models import BotUser

from .schemas import LastLocResponse, LastLocUpdateResponse, LastLoc, WeatherResponse
from .api_calls import SyncWeatherAPI


backauth = BackendAuth()
weather_api = SyncWeatherAPI()
weather_router = APIRouter(dependencies=[Depends(backauth)])


@weather_router.post("/user/loc/{user_id}", response_model=LastLocUpdateResponse)
def update_user_last_loc(user_id: int, location: LastLoc):
    if not BotUser.objects.filter(user_id=user_id).exists():
        return JSONResponse(status_code=400, content={"status": "error", "error": "No user with that ID exists"})

    user = BotUser.objects.get(user_id=user_id)
    city_name = ""
    if location.city:
        user.user_last_loc_name = location.city
        city_name = location.city
    else:
        user.user_last_loc_name = None
    if location.latitude:
        user.user_last_loc_lat = location.latitude
    else:
        user.user_last_loc_lat = None
    if location.longitude:
        user.user_last_loc_lon = location.longitude
    else:
        user.user_last_loc_lon = None

    if (location.latitude and location.longitude) and (not location.city):
        city_name = weather_api.get_city_name(lat=location.latitude, lon=location.longitude)
        user.user_last_loc_name = city_name

    user.save()
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "message": "Data successfully updated",
            "new_loc": city_name
        }
    )


@weather_router.get("/user/loc/{user_id}", response_model=LastLocResponse)
def get_user_last_loc(user_id: int):
    if not BotUser.objects.filter(user_id=user_id).exists():
        return JSONResponse(status_code=400, content={"status": "error", "error": "No user with that ID exists"})

    user = BotUser.objects.get(user_id=user_id)
    if user.user_last_loc_lat and user.user_last_loc_lon:
        last_location = {
            "city": user.user_last_loc_name,
            "latitude": user.user_last_loc_lat,
            "longitude": user.user_last_loc_lon
        }
    elif user.user_last_loc_name:
        last_location = {
            "city": user.user_last_loc_name
        }
    else:
        last_location = {
            "city": "Unknown"
        }
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "last_location": last_location
        }
    )


@weather_router.get("/weather/{user_id}", response_model=WeatherResponse)
def get_weather(user_id: int):
    if not BotUser.objects.filter(user_id=user_id).exists():
        return JSONResponse(status_code=400, content={"status": "error", "error": "No user with that ID exists"})

    user = BotUser.objects.get(user_id=user_id)
    location = {}

    if user.user_last_loc_lat and user.user_last_loc_lon:
        location["lat"] = user.user_last_loc_lat
        location["lon"] = user.user_last_loc_lon
    elif user.user_last_loc_name and not user.user_last_loc_name == "Unknown":
        location["city"] = user.user_last_loc_name
    else:
        return "Some error"

    weather = weather_api.get_weather(location)
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "weather": weather,
            "city": user.user_last_loc_name
        }
    )
