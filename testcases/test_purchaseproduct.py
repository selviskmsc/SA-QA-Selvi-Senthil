import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.PurchaseProduct import PurchaseProduct
#options = webdriver.ChromeOptions()
#chrome_options = options()

class Test_002_PurchaseProduct:
    baseURL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"



    def test_productpurchase(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.pp = PurchaseProduct(self.driver)
        self.pp.clickitem()
        time.sleep(5)

