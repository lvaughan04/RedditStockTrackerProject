from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://lvaughan:LUuJ6l24YNeBk7T6@redditstocktrackermenti.qbpw8.mongodb.net/"

client = MongoClient(CONNECTION_STRING)

db = client['Reddit Stock Tracker']