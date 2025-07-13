import time
from pageObjects.LoginPage import LoginPage
from pageObjects.PurchaseProduct import PurchaseProduct
from pageObjects.AddtoCart import AddToCart
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.PurchaseProduct import PurchaseProduct
from pageObjects.AddtoCart import AddToCart
from pageObjects.ShoppingCart import ShoppingCart



class Test_004_Shoppingcart:
    baseURL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"



    def test_shoppingcart(self,setup):
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



