class PurchaseProduct:
    label_text_xpath="//*[@id='item_4_title_link']/div"

    def __init__(self,driver):
        self.driver=driver

    def clickitem(self):
        self.driver.find_element("xpath",self.label_text_xpath).click()