import time
from pageObjects.LoginPage import LoginPage
from pageObjects.PurchaseProduct import PurchaseProduct
from pageObjects.AddtoCart import AddToCart
from pageObjects.CheckOut import Checkout
from pageObjects.ShoppingCart import ShoppingCart


class Test_005_Checkout():
    baseURL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"


    def test_checkout(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.pp = PurchaseProduct(self.driver)
        self.pp.clickitem()
        self.ac = AddToCart(self.driver)
        self.ac.clickaddtocart()
        self.sc = ShoppingCart(self.driver)
        self.sc.shoppingcart()
        self.check = Checkout(self.driver)
        self.check.clickcheckout()
        time.sleep(5)



