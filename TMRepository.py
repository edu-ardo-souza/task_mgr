import pymongo
from pymongo import MongoClient
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read('config.ini')

db_server = config_object['DATABASE']['SERVER']
db_port = config_object['DATABASE']['PORT']
db_name = config_object['DATABASE']['DB_NAME']
db_collection = config_object['DATABASE']['COLLECTION']

mongoClient = MongoClient(db_server, db_port)
mongoDb = mongoClient[db_name]
mongoCol = mongoDb[db_collection]