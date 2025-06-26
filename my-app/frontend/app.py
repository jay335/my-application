from flask import Flask, render_template, request
from datetime import datetime
import requests

BACKEND_URL = 'http://0.0.0.0:9000'
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    form_data = dict(request.form)
    try:
        response = requests.post(BACKEND_URL + '/submit', json=form_data)
        response.raise_for_status()  # raises HTTPError if response is not 200-299
        return "Data Submitted Successfully"
    except requests.exceptions.RequestException as e:
        return render_template('index.html', message=None, error=f"Error: {str(e)}")
    
@app.route('/get_data')
def get_data():
    response = requests.get(BACKEND_URL + '/view')
    return response.json()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)