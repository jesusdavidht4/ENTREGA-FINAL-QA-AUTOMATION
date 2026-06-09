import pytest
import logging
from utils.helpers import get_driver, take_screenshot

logger = logging.getLogger(__name__)

@pytest.fixture
def driver(request):
    driver = get_driver()
    yield driver
    
    # Screenshot automático si el test falló
    if request.node.rep_call.failed:
        logger.warning(f"Test fallido: {request.node.name} — tomando screenshot")
        take_screenshot(driver, request.node.name)
    
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

@pytest.fixture
def api_user_data():
    return {
        "name": "Jesus David",
        "job": "QA Automation"
    }

#def reporte_html_report_titule( reporte ):
#   reporte.titule = "API - REQUERES PYTEST WITH REQUEST"