import time


class AddToCart:
    button_id="add-to-cart"

    def __init__(self,driver):
        self.driver=driver

    def clickaddtocart(self):
        self.driver.find_element("id", self.button_id).click()
