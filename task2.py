# Importing libraries.
from flask import Flask, jsonify, request,make_response
import json
from flask_cors import CORS, cross_origin
import requests
import validators
app = Flask(__name__)

# Function for info endpoint. Only GET method is allowed for this endpoint.
@app.route('/info', methods=['GET'])
def info():
    # Sending a message to enduser.
    result = {"Receiver": "Cisco is the best!"}
    return jsonify(result)

# Function for ping endpoint. Only POST is allowed.
@app.route('/ping', methods=['POST'])
def ping():
    if request.method == 'POST':
        # Getting request body from user.
        request_body = request.json
        # Checking if request body is not empty and contains url key.
        if request_body==None or 'url' not in request_body:
            # If it does not, sending proper error message.
            return make_response(jsonify({"error":"Please provide url in request body"}), 400)
        else:
            # Getting url from body.
            url = request_body["url"]
            # Validating URL. 
            url_validate = validators.url(url)
            if url_validate:
                # Sending request to url defined in body (Skipping SSL).
                req = requests.get(url, verify=False)
                
                # Returning response to enduser.
                return make_response(req.content, 200)
            else:
                # In case of user does not provide correct URL.
                return make_response(jsonify({"error":"Please provide valid url in request body"}), 400)

app.run(host='0.0.0.0', debug=True, port=8000)
