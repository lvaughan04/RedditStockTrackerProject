from pymongo import MongoClient, errors
import certifi
from config import CONNECTION_STRING
    
def setup_database():
    try:
        client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
        db = client["StockData"]

        print(client.server_info()["version"])

        # for doc in db["Posts"].find({}, {"timestamp": 1}):
        #     print(doc)
        
        # Ensure the Posts collection exists before initializing the collections
        if "Posts" not in db.list_collection_names():
            db.create_collection(
                "Posts",
                timeseries={
                    "timeField": "timestamp",  
                    "metaField": "metadata",   
                    "granularity": "hours"
                }
            )

            db["Posts"].create_index(
            [("timestamp", 1)],  
            expireAfterSeconds=20, 
            partialFilterExpression={"metadata": {"$exists": True}} 
        )
            print("Time series collection 'Posts' created.")
        else:
            print("Time series collection 'Posts' already exists.")

        indexes = db["Posts"].index_information()

        for index in indexes.values():
            print(index)

        # Alternatively, you can check for a specific TTL index on the "timestamp" field:
        ttl_index_exists = False

        for index in indexes.values():
            if index.get("key") == [("timestamp", 1)] and index.get("expireAfterSeconds") == 20:
                ttl_index_exists = True
                print("TTL index exists and is correctly configured.")
                break

        if not ttl_index_exists:
            print("TTL index does not exist or is misconfigured.")

        # Initialize the collections after ensuring they exist
        SP_COLLECTION = db["SP500"]
        POSTS_COLLECTION = db["Posts"]

        return SP_COLLECTION, POSTS_COLLECTION

    except errors.PyMongoError as e:
        print("Failed to Connect to Database:", e)
        return None, None    



SP_COLLECTION, POSTS_COLLECTION = setup_database()


