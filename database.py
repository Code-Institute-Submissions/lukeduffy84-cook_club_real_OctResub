import os
from dotenv import load_dotenv

load_dotenv()

import pymongo

client = pymongo.MongoClient(os.getenv('MONGODB'))
db = client["cook_club"]
# print(db.list_collection_names())
