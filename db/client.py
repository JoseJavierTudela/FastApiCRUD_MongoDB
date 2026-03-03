from pymongo import MongoClient
from pymongo.server_api import ServerApi

#base de datos local
# db_client = MongoClient().local


uri = "mongodb+srv://jjtudela:SaulHudson18@db.lbajmfd.mongodb.net/?appName=DB"
# Create a new MongoClient and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# select the desired database name that your Atlas user has access to
# 'local' is typically not writable by remote users; choose a custom DB name
# e.g. create a database named 'FastApiCRUD' in Atlas and grant your user rights

#db_client = client.local  # avoid using the internal 'local' database

# use get_database for clarity and explicitness

db_client = client.get_database('FastApiCRUD')