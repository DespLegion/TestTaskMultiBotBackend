from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from .schemas import TestingSchema
from fastapi_utils.auth import BackendAuth
from fastapi_utils.testing_generator import TestingGen


backauth = BackendAuth()
testings_gen = TestingGen()
testing_router = APIRouter(dependencies=[Depends(backauth)])


@testing_router.get("/testing", response_model=TestingSchema)
def get_new_testing():
    try:
        testings = testings_gen.generate()
        return JSONResponse(status_code=200, content={"status": "success", "testing": testings})
    except Exception as err:
        return JSONResponse(status_code=500, content={"status": "error", "testing": f"Error: {err}"})
