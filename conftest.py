import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os

@pytest.fixture(scope="function")
def driver(request):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Uncomment if headless is desired
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    
    yield driver
    
    # Capture screenshot on failure
    if request.node.rep_call.failed:
        try:
            if not os.path.exists('screenshots'):
                os.makedirs('screenshots')
            driver.save_screenshot(f"screenshots/{request.node.name}.png")
        except Exception as e:
            print(f"Failed to save screenshot: {e}")

    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    
    # Set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
