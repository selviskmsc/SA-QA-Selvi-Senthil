
from selenium.webdriver.common.by import By
class ContinuePage:
    textbox_firstname_id="first-name"
    textbox_lastname_id="last-name"
    textbox_zip_id="postal-code"
    button_continue_id="continue"

    def __init__(self,driver):
        self.driver=driver

    def setfirstname(self,firstname):
        self.driver.find_element("id", self.textbox_firstname_id).clear()
        self.driver.find_element("id", self.textbox_firstname_id).send_keys(firstname)

    def setlastname(self,lastname):
        self.driver.find_element("id", self.textbox_lastname_id).clear()
        self.driver.find_element("id", self.textbox_lastname_id).send_keys(lastname)

    def setzip(self,zip):
        self.driver.find_element("id", self.textbox_zip_id).clear()
        self.driver.find_element("id", self.textbox_zip_id).send_keys(zip)

    def clickContinue(self):
        self.driver.find_element("id", self.button_continue_id).click()


