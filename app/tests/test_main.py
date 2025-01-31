import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI with Celery and Docker Compose"}


@patch("main.create_task.delay")
def test_run_task(mock_create_task):
    mock_create_task.return_value.id = "mock_task_id"

    response = client.post("/tasks/test_data")

    assert response.status_code == 200
    assert response.json() == {"task_id": "mock_task_id", "status": "Processing"}


@patch("main.collection.find")
def test_get_all_tasks(mock_find):
    mock_find.return_value = [{"data": "test", "status": "completed"}]

    response = client.get("/tasks/")

    assert response.status_code == 200
    assert response.json() == {"tasks": [{"data": "test", "status": "completed"}]}
