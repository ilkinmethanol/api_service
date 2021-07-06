### Flask API Service
Basic HTTP application using a python web framework (Flask)

Docker Installation
$ git clone https://github.com/ilkinmethanol/api_service.git
$ cd api_service
$ docker-compose build
$ docker-compose up -d

Manual installation:
$ git clone https://github.com/ilkinmethanol/api_service.git
$ cd api_service
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ export FLASK_APP=task2.py
$ flask run

### Endpoints
- GET /info
returns hardcoded status of `{“Receiver”: “Cisco is the best!”}`
- POST /ping
Used for returning entries of corresponding link, ie `{‘url’: 'https:/example.com'}` by skipping SSL.

### Usage:
`curl -iX POST http://127.0.0.1:5000/ping -d '{"url":"https://google.com"}' --header 'Content-Type: application/json'
`

`curl -iX GET http://127.0.0.1:5000/info`
