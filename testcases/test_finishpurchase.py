import time
from pageObjects.LoginPage import LoginPage
from pageObjects.PurchaseProduct import PurchaseProduct
from pageObjects.AddtoCart import AddToCart
from pageObjects.CheckOut import Checkout
from pageObjects.ShoppingCart import ShoppingCart
from pageObjects.Continue import ContinuePage
from pageObjects.FinishPurchase import FinishPurchase


class Test_003_AddtoCart():
    baseURL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    firstname = "selvi"
    lastname = "s"
    zip = 600129

    def test_finishpurchase(self,setup):
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
        self.cp = ContinuePage(self.driver)
        self.cp.setfirstname(self.firstname)
        self.cp.setlastname(self.lastname)
        self.cp.setzip(self.zip)
        self.cp.clickContinue()
        self.fp = FinishPurchase(self.driver)
        self.fp.clickFinish()

