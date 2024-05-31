from model.Task import Task
from pymongo import MongoClient
from configparser import ConfigParser
from fastapi.encoders import jsonable_encoder

config_object = ConfigParser()
config_object.read('config.ini')

db_server = config_object['DATABASE']['SERVER']
db_port = int(config_object['DATABASE']['PORT'])
db_name = config_object['DATABASE']['DB_NAME']
db_collection = config_object['DATABASE']['COLLECTION']

mongoClient = MongoClient(db_server, db_port)
mongoDb = mongoClient[db_name]
mongoCol = mongoDb[db_collection]

def list():
    return mongoCol.find()

def create(task : Task):
    return mongoCol.insert_one(task)

# ToBeDone: raise task not found exception
def update(task_id : str, task : Task):
    return mongoCol.update_one({"_id":task_id},{"$set": task}, upsert=False)

# ToBeDone: raise task not found exception
def delete(id : str):
    return mongoCol.delete_one({"_id": id})