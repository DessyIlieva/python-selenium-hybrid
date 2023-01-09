from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:

    usernameField = (By.ID, 'inputUsername')
    passowrdField = (By.ID, 'loginpassword')
    loginButton = (By.XPATH, '//input[@value="Login"]')
    logOutButton = (By.LINK_TEXT, 'Log Out')
    addBookButton = (By.XPATH, "//a[.='Add Book']" )

    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,usernameData):
        username = self.driver.find_element(*self.usernameField)
        username.clear()
        username.send_keys(usernameData)


    def setPassword(self, passwordData):
        password = self.driver.find_element(*self.passowrdField)
        password.clear()
        password.send_keys(passwordData)


    def clickLogin(self):
        login = self.driver.find_element(*self.loginButton)
        login.click()

    def clickLogout(self):
        logout = self.driver.find_element(*self.logOutButton)
        logout.click()

    def addBookButtonPresent(self):
        addBookPresent = False
        addBook = self.driver.find_elements(*self.addBookButton)
        if len(addBook) > 0:
            addBookPresent = True
        return addBookPresent