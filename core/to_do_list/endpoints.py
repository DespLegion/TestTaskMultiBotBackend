from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from core.bot_users.models import BotUser
from .models import TasksModel
from .schemas import TaskSchema, AllTasksSchema, TaskPostSchema, GetCurTaskSchema
from fastapi_utils.auth import BackendAuth


backauth = BackendAuth()
to_do_list_router = APIRouter(dependencies=[Depends(backauth)])


@to_do_list_router.get("/to_do/{user_id}", response_model=AllTasksSchema)
def get_all_user_tasks(user_id: int):
    if not BotUser.objects.filter(user_id=user_id).exists():
        return JSONResponse(status_code=400, content={"status": "error", "message": "No user with that ID exists"})

    try:
        user_tasks = TasksModel.objects.filter(user__user_id=user_id)
        res = []
        for task in user_tasks:
            res.append(
                {
                    "task_id": task.pk,
                    "task_title": task.task_title,
                    "task_text": task.task_text,
                }
            )
        return JSONResponse(status_code=200, content={"status": "success", "user_tasks": res})
    except Exception as err:
        return JSONResponse(status_code=500, content={"status": "error", "user_tasks": err})


@to_do_list_router.post("/to_do/{user_id}", response_model=TaskPostSchema)
def create_user_task(user_id: int, task: TaskSchema):
    if not BotUser.objects.filter(user_id=user_id).exists():
        return JSONResponse(status_code=400, content={"status": "error", "message": "No user with that ID exists"})

    try:
        user = BotUser.objects.get(user_id=user_id)
        new_task = TasksModel()
        new_task.task_title = task.task_title
        new_task.task_text = task.task_text
        new_task.user = user
        new_task.save()
        return JSONResponse(status_code=200, content={"status": "success", "message": "New task successfully added"})
    except Exception as err:
        return JSONResponse(status_code=500, content={"status": "error", "message": err})


@to_do_list_router.get("/to_do/{user_id}/{task_id}", response_model=GetCurTaskSchema)
def get_user_task(user_id: int, task_id: int):
    if not BotUser.objects.filter(user_id=user_id).exists():
        return JSONResponse(status_code=400, content={"status": "error", "message": "No user with that ID exists"})
    try:
        task = TasksModel.objects.get(user__user_id=user_id, pk=task_id)
        res = {
            "task_title": task.task_title,
            "task_text": task.task_text
        }
        return JSONResponse(status_code=200, content={"status": "success", "message": res})
    except Exception as err:
        return JSONResponse(status_code=500, content={"status": "error", "message": f"Error: {err}"})


@to_do_list_router.patch("/to_do/{user_id}/{task_id}", response_model=TaskPostSchema)
def update_user_task(user_id: int, task_id: int, task: TaskSchema):
    if not BotUser.objects.filter(user_id=user_id).exists():
        return JSONResponse(status_code=400, content={"status": "error", "message": "No user with that ID exists"})
    try:
        task_to_update = TasksModel.objects.get(user__user_id=user_id, pk=task_id)
        if task.task_title:
            task_to_update.task_title = task.task_title
        if task.task_text:
            task_to_update.task_text = task.task_text
        task_to_update.save()
        return JSONResponse(status_code=200, content={"status": "success", "message": "Task updated successfully"})
    except Exception as err:
        return JSONResponse(status_code=500, content={"status": "error", "message": f"Error: {err}"})


@to_do_list_router.delete("/to_do/{user_id}/{task_id}", response_model=TaskPostSchema)
def delete_user_task(user_id: int, task_id: int):
    if not BotUser.objects.filter(user_id=user_id).exists():
        return JSONResponse(status_code=400, content={"status": "error", "message": "No user with that ID exists"})
    try:
        task_to_delete = TasksModel.objects.get(user__user_id=user_id, pk=task_id)
        task_to_delete.delete()
        return JSONResponse(status_code=200, content={"status": "success", "message": "Task deleted successfully"})
    except Exception as err:
        return JSONResponse(status_code=500, content={"status": "error", "message": f"Error: {err}"})
