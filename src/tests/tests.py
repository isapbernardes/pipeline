import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get('/')
    assert b'Welcome to the Shop!' in rv.data

def test_login(client):
    rv = client.post('/login', data=dict(
        username='admin',
        password='password'
    ))
    assert rv.status_code == 302
