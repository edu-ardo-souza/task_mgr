from loguru import logger
import repository
from  model.Task import Task
import sys

logger.remove()
logger.add(sys.stdout, level="INFO")

def list():
    logger.info("Listing all tasks.")
    return repository.list()

def create(task : Task):
    logger.info("Creating new task : " + task)
    return repository.create(task)

def update(task_id : str, task : Task):
    logger.info("Updating existing task")
    return repository.update(task_id, task)

def delete(id : str):
    logger.info("Deleting task id : " + id)
    return repository.delete(id)