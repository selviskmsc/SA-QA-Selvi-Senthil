from selenium import webdriver
import pytest
from selenium.webdriver.edge.service import Service as EdgeService # Optional, for service-based instantiation



@pytest.fixture()
def setup(browser):
    # chromedriver_path = 'D:/selvi/chromedriver-win64/chromedriver-win64/chromedriver.exe'
    edgeDriverPath = 'D:/selvi/EdgeDriver/msedgedriver.exe'
    service = EdgeService(executable_path=edgeDriverPath)


    #Initialize the Chrome WebDriver
    # driver = webdriver.Chrome(service=service)
    driver = webdriver.Edge(service=service)
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# def pytest_configure(config):
#     config._metadata['Project Name'] = 'SA-QA-SelviSenthil'
#     config._metadata['Module Name'] = 'Add to Cart'
#     config._metadata['Tester'] = 'SelviSenthil'

#@pytest.mark.optionalhook
#def pytest_metadata(metadata):
    #metadata.pop("JAVA HOME",None)
    #metadata.pop("Plugins", None)




