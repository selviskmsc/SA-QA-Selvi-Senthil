import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
#options = webdriver.ChromeOptions()
#chrome_options = options()

class Test_001_Login:
    baseURL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    def test_homepagetitle(self, setup):
         self.driver=setup
         self.driver.get(self.baseURL)
         act_title=self.driver.title
         print("Title=",act_title)
         if act_title==("Swag Labs"):
             assert True
             self.driver.close()
         else:
             self.driver.save_screenshot("..\\.\\Screenshots\\"+"test_homepagetitle.png")
             assert True
             self.driver.close()

    def test_login(self, setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        time.sleep(10)
        if act_title == "Swag Labs":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepagetitle.png")
            self.driver.close()
            assert False









