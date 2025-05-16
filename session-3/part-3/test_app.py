import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Simple Calculator' in response.data

def test_add_get(client):
    response = client.get('/add?num1=10&num2=5')
    assert response.status_code == 200
    assert response.get_json()['result'] == 15.0

def test_add_post(client):
    response = client.post('/add', json={'num1': 10, 'num2': 5})
    assert response.status_code == 200
    assert response.get_json()['result'] == 15.0

def test_subtract(client):
    response = client.get('/subtract?num1=10&num2=5')
    assert response.status_code == 200
    assert response.get_json()['result'] == 5.0

def test_multiply(client):
    response = client.get('/multiply?num1=10&num2=5')
    assert response.status_code == 200
    assert response.get_json()['result'] == 50.0

def test_divide(client):
    response = client.get('/divide?num1=10&num2=5')
    assert response.status_code == 200
    assert response.get_json()['result'] == 2.0

def test_metrics(client):
    response = client.get('/metrics')
    assert response.status_code == 200
    assert b'python_request_operations_total' in response.data
