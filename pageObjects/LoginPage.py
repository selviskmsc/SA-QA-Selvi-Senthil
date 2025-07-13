from selenium.webdriver.common.by import By
class LoginPage:
    textbox_username_id="user-name"
    textbox_password_id="password"
    button_login_id="login-button"

    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,username):
        self.driver.find_element("id", self.textbox_username_id).clear()
        self.driver.find_element("id", self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element("id", self.textbox_password_id).clear()
        self.driver.find_element("id", self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element("id", self.button_login_id).click()







