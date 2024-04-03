from pydantic import BaseModel
from typing import List


class TestingAnswers(BaseModel):
    r_answer: int
    f_answer_1: int
    f_answer_2: int
    f_answer_3: int


class Testing(BaseModel):
    question: str
    answers: TestingAnswers


class TestingSchema(BaseModel):
    status: str
    testing: List[Testing] | str

