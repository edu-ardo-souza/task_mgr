from fastapi import FastAPI, Body, status, Request
from fastapi.encoders import jsonable_encoder
import service as service
from model.Task import Task

app = FastAPI()

@app.get("/list", response_description="List all tasks", status_code=status.HTTP_200_OK, response_model=list)
async def list():
    return service.list()

@app.post("/create", response_description="Create a new task", status_code=status.HTTP_201_CREATED, response_model=Task)
def create(request: Request, task : Task = Body(...)):
    task = jsonable_encoder(task)
    return service.create(task)

# ToBeDone: fix proper functioning of update
@app.patch("/update/{task_id}", response_description="Update an existing task", status_code=status.HTTP_200_OK, response_model=Task)
async def update(request: Request, task_id : str, task : Task = Body(...)):
    task = jsonable_encoder(task)
    return service.update(task_id, task)

# ToBeDone: fix proper functioning of delete
@app.delete("/delete", response_description="Delete an existing task", status_code=status.HTTP_200_OK)
async def delete(request: Request, id : str = Body(...)):
    return service.delete(id)

# ToBeDone: get task by ID