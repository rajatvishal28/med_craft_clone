from fastapi import FastAPI 
from models import HVACDetials
from pymongo import MongoClient
import datetime

app = FastAPI()

client = MongoClient()
target_db = client.hvac_automation

@app.post("/add_data")
async def add_details(body : HVACDetials):
    try: 
        details = body.dict() 
        collection = target_db.people_count_data
        details['timestamp'] = datetime.datetime.now()
        collection.insert(details)
        return {
            "status": 200,
            "data" : [],
            "message" : "Data Registered"
        }
    except: 
        return {
            "status" : 400,
            "data" : [],
            "message" : "Some Error Occured"
        } 
    

@app.post("/get_data") 
def get_details(): 
    try: 
        collection = target_db.people_count_data
        data = []
        for i in collection.find({}, {'_id': 0}):
            data.append(i)
        print(data)
        return {
            "status": 400,
            "data": data,
            "message": "Data Found"
        }
    except: 
        return {
            "status": 400,
            "data": [],
            "message": "Some Error Occured"
        }