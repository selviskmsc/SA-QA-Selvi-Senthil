from selenium.webdriver.common.by import By
class Checkout:
    button_checkout_id="checkout"

    def __init__(self,driver):
        self.driver=driver

    def clickcheckout(self):
        self.driver.find_element("id", self.button_checkout_id).click()

