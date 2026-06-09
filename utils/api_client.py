import requests
import logging

logger = logging.getLogger(__name__)

BASE_URL = "https://reqres.in/api"
HEADERS = {
    "x-api-key": "pro_e810da006a341cf0dd53779a9c27b6193156b3c423a0e5733ca3f845438d7efd",
    "X-Reqres-Env": "prod"
}

def get_users(page=1):
    logger.info(f"GET usuarios - página {page}")
    return requests.get(f"{BASE_URL}/users", params={"page": page}, headers=HEADERS)

def create_user(name, job):
    logger.info(f"POST crear usuario: {name}, {job}")
    return requests.post(f"{BASE_URL}/users", json={"name": name, "job": job}, headers=HEADERS)

def delete_user(user_id):
    logger.info(f"DELETE usuario id: {user_id}")
    return requests.delete(f"{BASE_URL}/users/{user_id}", headers=HEADERS)

def update_user(name, job, user_id):
    logger.info(f"PUT actualizar usuario id: {user_id}")
    return requests.put(f"{BASE_URL}/users/{user_id}", json={"name": name, "job": job}, headers=HEADERS)