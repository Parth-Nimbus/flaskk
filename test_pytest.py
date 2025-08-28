import pytest
from flask import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_helloworld_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello World!' in response.data
    assert b'Welcome to my Flask web app.' in response.data

def test_process_route_success(client):
    payload = {"name": "Parth"}
    response = client.post('/process', json=payload)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["message"] == "Hello Parth! Data received successfully."

#'''
def test_process_route_missing_name(client):
    payload = {}
    response = client.post('/process', json=payload)
    # Should raise a KeyError, so let's check for 500 error
    # print(response.text)
    print(response.status_code)
    assert response.status_code == 500
#'''