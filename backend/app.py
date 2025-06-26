from flask import Flask, request
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = MongoClient(os.getenv("MONGODB_URI"))
db = client.test
collection = db['flask-mongo-app']

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item = {
        "itemName": request.form['itemName'],
        "itemDescription": request.form['itemDescription']
    }
    collection.insert_one(item)
    return "Item submitted!"

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=9000,debug=True)
