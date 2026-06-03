import csv
import json
import logging
import os
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# ── Logging ──────────────────────────────────────────────────────────────────
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/test_run.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# ── Driver ────────────────────────────────────────────────────────────────────
def get_driver():
    logger.info("Iniciando ChromeDriver")
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-save-password-bubble")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# ── Carga de datos ────────────────────────────────────────────────────────────
def load_user_json(path):
    logger.info(f"Cargando usuarios desde JSON: {path}")
    users = []
    with open(path, encoding="utf-8") as file:
        data = json.load(file)
        for user in data:
            users.append((user["username"], user["password"]))
    return users

def load_user_csv(path):
    logger.info(f"Cargando datos desde CSV: {path}")
    rows = []
    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(tuple(row.values()))
    return rows

# ── Screenshots ───────────────────────────────────────────────────────────────
def take_screenshot(driver, test_name):
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshots/{test_name}_{timestamp}.png"
    driver.save_screenshot(filename)
    logger.info(f"Screenshot guardado: {filename}")
    return filename