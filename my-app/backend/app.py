from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
print(MONGO_URI)

app = Flask(__name__)

# Create a new client and connect to the server
client = MongoClient(MONGO_URI)
db = client.test
collection = db['flask-mongo-app']
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

@app.route('/submit',methods=['POST'])
def submit():
    form_data = dict(request.json)
    collection.insert_one(form_data)
    return "Data Submitted Successfully"

@app.route('/view')
def view():
    data = collection.find()
    data = list(data)
    for item in data:
        print(item)
        del item['_id']
    data = {
        'data' : data
    }
    return jsonify(data)

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=9000,debug=True)