from pydantic import BaseModel
from typing import Optional


class LastLocName(BaseModel):
    city: str


class LastLoc(BaseModel):
    city: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]


class LastLocResponse(BaseModel):
    status: str
    last_location: LastLocName | LastLoc


class LastLocUpdateResponse(BaseModel):
    status: str
    message: str
    new_loc: str


class BaseWeather(BaseModel):
    cur_temp: int
    temp_feels_like: int
    cloud: int
    wind_speed: float


class WeatherResponse(BaseModel):
    status: str
    weather: BaseWeather
    city: str
