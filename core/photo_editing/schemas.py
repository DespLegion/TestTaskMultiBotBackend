from pydantic import BaseModel


class WatermarkUpdateResp(BaseModel):
    status: str
    message: str
