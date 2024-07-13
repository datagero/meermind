from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os, logging

logger = logging.getLogger(__name__);

uri = os.environ.get("DB_CONNECTION_CONNECTION_STRING");

db_client = MongoClient(uri, server_api=ServerApi('1'))


def connect():
    # Create a new client and connect to the server
    try:
        db_client.admin.command('ping')
        logger.debug(f'database pinged')
    except Exception as e:
        print(e)


'''
{
    "title": "",
    "oneLineSummary": "",
    "studentSummary": [
        {
            "summaryTitle": "",
            "summaryPoints": [ "", ]
        },
        {
            "summaryTitle": "",
            "summaryPoints": [
                "",
                ""
            ]
        }
    ],
    "relatedInformation": [],
    "benefits": [],
    "limitations": [],
    "realWorldExample": "",
    "stateOfTheArtResearch": "",
    "references": []
}
'''

def save():

    pass



