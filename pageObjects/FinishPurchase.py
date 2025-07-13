class FinishPurchase:
    button_finish_id="finish"

    def __init__(self, driver):
        self.driver = driver

    def clickFinish(self):
        self.driver.find_element("id", self.button_finish_id).click()