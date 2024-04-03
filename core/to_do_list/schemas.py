from pydantic import BaseModel
from typing import Optional


class TaskPostSchema(BaseModel):
    status: str
    message: str


class TaskSchema(BaseModel):
    task_title: Optional[str]
    task_text: Optional[str]


class TaskRespSchema(BaseModel):
    task_id: int
    task_title: str
    task_text: str


class GetCurTaskSchema(BaseModel):
    status: str
    message: TaskSchema | str


class AllTasksSchema(BaseModel):
    status: str
    user_tasks: Optional[list[TaskRespSchema]] | str
