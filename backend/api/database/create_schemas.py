import os
import json
from pymongo import MongoClient
from bson.binary import Binary
from dotenv import load_dotenv

# Load config from a .env file:
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

# Replace the following with your MongoDB Atlas connection string
connection_string = MONGODB_URI
client = MongoClient(connection_string)

# Create a database
db_name = "meermind_v01"
db = client[db_name]

# =============================================================================
# Create the transcript collection
collection_name = "transcript"
transcript_collection = db[collection_name]

# Insert and remove a dummy document to create the collection
transcript_collection.insert_one({"_id": "dummy"})
transcript_collection.delete_one({"_id": "dummy"})

# Load and apply the schema from JSON file
schema_file = "backend/database/schemas/transcript_schema.json"
with open(schema_file, 'r') as file:
    schema = json.load(file)
    db.command("collMod", collection_name, validator=schema)

# Create indexes for module_name, file_name, and file_ext
transcript_collection.create_index("document_hash_id")

# =============================================================================
# Create the transcript_summary collection
collection_name = "transcript_summary_schema"
transcript_summary_collection = db[collection_name]

# Insert and remove a dummy document to create the collection
transcript_summary_collection.insert_one({"_id": "dummy"})
transcript_summary_collection.delete_one({"_id": "dummy"})

schema_file = "backend/database/schemas/transcript_summary_schema.json"
with open(schema_file, 'r') as file:
    schema = json.load(file)
    db.command("collMod", collection_name, validator=schema)

# Create indexes for module_name, file_name, and file_ext
transcript_summary_collection.create_index("document_hash_id")

# =============================================================================
# Create the document_hash_id collection
collection_name = "document_hash_id"
document_hash_id_collection = db[collection_name]

# Insert and remove a dummy document to create the collection
document_hash_id_collection.insert_one({"_id": "dummy"})
document_hash_id_collection.delete_one({"_id": "dummy"})

schema_file = "backend/database/schemas/document_hash_id_schema.json"
with open(schema_file, 'r') as file:
    schema = json.load(file)
    db.command("collMod", collection_name, validator=schema)

# Create indexes for module_name, file_name, and file_ext
document_hash_id_collection.create_index("document_hash_id")

# =============================================================================
print("Collection created successfully with schema applied!")
