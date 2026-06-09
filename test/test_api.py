import pytest
import logging
import os
from utils.api_client import get_users, create_user, delete_user, update_user

logger = logging.getLogger(__name__)

def test_get_users():
    logger.info("Test GET: obtener lista de usuarios")
    response = get_users(page=1)

    assert response.status_code == 200

    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0
    assert "id" in data["data"][0]
    assert "email" in data["data"][0]

def test_create_user(api_user_data):
    logger.info("Test POST: crear usuario")
    response = create_user(api_user_data["name"], api_user_data["job"])

    assert response.status_code == 201

    body = response.json()
    assert body["name"] == api_user_data["name"]
    assert body["job"] == api_user_data["job"]
    assert "id" in body
    assert "createdAt" in body

def test_delete_user():
    logger.info("Test DELETE: eliminar usuario")
    response = delete_user(user_id=2)

    assert response.status_code == 204
    assert response.text == ""

def test_update_user():
    logger.info("Test PUT: actualizar usuario")
    response = update_user("Jesus", "QA Automation", 2)

    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Jesus"
    assert body["job"] == "QA Automation"