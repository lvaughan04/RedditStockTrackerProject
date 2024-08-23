from pymongo import MongoClient, ASCENDING, errors
import certifi
from config import CONNECTION_STRING
    
def setup_database():
    try:
        client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
        db = client["StockData"]

        # Ensure the Posts collection exists before initializing the collections
        if "Posts" not in db.list_collection_names():
            db.create_collection(
                "Posts",
                timeseries={
                    "timeField": "timestamp",  
                    "metaField": "stock_symbol",   
                    "granularity": "hours"     
                }
            )
            print("Time series collection 'Posts' created.")
        else:
            print("Time series collection 'Posts' already exists.")

        # Initialize the collections after ensuring they exist
        SP_COLLECTION = db["SP500"]
        POSTS_COLLECTION = db["Posts"]

        # Ensure the TTL index exists
        db["Posts"].create_index(
            [("timestamp", ASCENDING)],
            expireAfterSeconds=86400,  # 24 hours = 86400 seconds
            partialFilterExpression={"stock_symbol": {"$exists": True}}
        )
        print("TTL index created or verified.")

        return SP_COLLECTION, POSTS_COLLECTION

    except errors.PyMongoError as e:
        print("Failed to Connect to Database:", e)
        return None, None    



SP_COLLECTION, POSTS_COLLECTION = setup_database()


