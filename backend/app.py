from flask import Flask, request, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend/templates'))
app = Flask(__name__, template_folder=template_dir)

client = MongoClient(os.getenv("MONGODB_URI"))
db = client.test
collection = db['flask-mongo-app']

@app.route("/")
def todo_form():
    return render_template("index.html")

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
