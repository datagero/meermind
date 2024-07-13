import os
import logging
import json
from pymongo import MongoClient
from bson.binary import Binary
from dotenv import load_dotenv

logger = logging.getLogger(__name__);

# Load config from a .env file:
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

# Replace the following with your MongoDB Atlas connection string
connection_string = MONGODB_URI
client = MongoClient(connection_string)

# Create a database
db_name = "meermind_v01"
db = client[db_name]

# Retrieve the transcript collection
transcript_collection = db["transcript"]
transcript_summary_collection = db["transcript_summary"]

def connect():
    # Create a new client and connect to the server
    try:
        client.admin.command('ping')
        logger.debug(f'database pinged')
    except Exception as e:
        print(e)


# Function to insert file data and metadata
def insert_transcript(module_name, file_name, file_ext, file_data):

    filter_criteria = {
        "module_name": module_name,
        "file_name": file_name,
        "file_ext": file_ext
    }
    update_data = {
        "$set": {
            "file_data": Binary(file_data)
        }
    }
    result = transcript_collection.update_one(filter_criteria, update_data, upsert=True)

    if result.upserted_id:
        print(f"Inserted summary document for file {module_name}:{file_name}{file_ext}")
    else:
        print(f"Updated summary document for file {module_name}:{file_name}{file_ext}")


# Function to insert file data and metadata
def insert_transcript_summary(module_name, file_name, file_ext, json_data):

    filter_criteria = {
        "module_name": module_name,
        "file_name": file_name,
        "file_ext": file_ext
    }
    update_data = {
        "$set": json_data
    }

    result = transcript_summary_collection.update_one(filter_criteria, update_data, upsert=True)

    if result.upserted_id:
        print(f"Inserted summary document for file {module_name}:{file_name}{file_ext}")
    else:
        print(f"Updated summary document for file {module_name}:{file_name}{file_ext}")

def clean_collection(connection_string, db_name, collection_name):
    # Connect to MongoDB Atlas
    client = MongoClient(connection_string)
    db = client[db_name]
    collection = db[collection_name]

    # Delete all documents in the collection
    result = collection.delete_many({})
    print(f"Deleted {result.deleted_count} documents from the {collection_name} collection.")

def careful_clean_collections():
    # # # Clean Collections
    # # clean_collection(connection_string, db_name, "transcript")
    # # clean_collection(connection_string, db_name, "transcript_summary")
    pass