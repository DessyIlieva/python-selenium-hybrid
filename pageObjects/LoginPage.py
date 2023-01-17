from selenium.webdriver.common.by import By

class LoginPage:

    usernameField = (By.ID, 'inputUsername')
    passwordField = (By.ID, 'loginpassword')
    loginButton = (By.XPATH, '//input[@value="Login"]')

    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,usernameData):
        username = self.driver.find_element(*self.usernameField)
        username.clear()
        username.send_keys(usernameData)


    def setPassword(self, passwordData):
        password = self.driver.find_element(*self.passwordField)
        password.clear()
        password.send_keys(passwordData)


    def clickLogin(self):
        login = self.driver.find_element(*self.loginButton)
        login.click()