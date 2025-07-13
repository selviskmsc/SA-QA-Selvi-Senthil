class ShoppingCart:
    button_shoppingcart_xpath="//a[@class='shopping_cart_link']"

    def __init__(self,driver):
        self.driver=driver

    def shoppingcart(self):
        self.driver.find_element("xpath", self.button_shoppingcart_xpath).click()
