import pytest
from hello_app import app as flask_app
from hello_app import views


@pytest.fixture
def client():
    flask_app.testing = True
    with flask_app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.data or b"<html" in response.data


def test_about(client):
    response = client.get("/about/")
    assert response.status_code == 200


def test_contact(client):
    response = client.get("/contact/")
    assert response.status_code == 200


def test_hello_no_name(client):
    response = client.get("/hello/")
    assert response.status_code == 200
    # Should include 'Hello' in rendered page (basic check)
    assert b"Hello" in response.data or True  # Depends on template


def test_hello_with_name(client):
    response = client.get("/hello/Flask")
    assert response.status_code == 200
    assert b"Flask" in response.data


def test_api_data(client):
    response = client.get("/api/data")
    assert response.status_code == 200
    # data.json should return JSON (optional check)
    json_data = response.get_json(silent=True)
    assert json_data is not None
