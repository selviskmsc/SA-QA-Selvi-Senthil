from selenium import webdriver
import pytest
from selenium.webdriver.edge.service import Service as EdgeService # Optional, for service-based instantiation



@pytest.fixture()
def setup():
    # chromedriver_path = 'D:/selvi/chromedriver-win64/chromedriver-win64/chromedriver.exe'
    edgeDriverPath = 'D:/selvi/EdgeDriver/msedgedriver.exe'
    service = EdgeService(executable_path=edgeDriverPath)


    #Initialize the Chrome WebDriver
    # driver = webdriver.Chrome(service=service)
    driver = webdriver.Edge(service=service)
    return driver


