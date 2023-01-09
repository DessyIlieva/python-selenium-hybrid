import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from datetime import datetime


class Test_001_Login:
    baseURL = "http://bookswappers.pythonanywhere.com/users/login"
    usernameData = "test2"
    passwordData = "lotlorien"

    
    def test_userLoggedOut(self, setup):
        self.driver = setup
        self.driver.maximize_window()        
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)

        # Verify Add Book button is NOT visible
        if self.lp.addBookButtonPresent():
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_userLoggedOut.png")
            self.driver.close()
            assert False
        

    def test_userLogin(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.usernameData)
        self.lp.setPassword(self.passwordData)
        self.lp.clickLogin()

        # Verify Add Book button is visible
        if self.lp.addBookButtonPresent():
            self.driver.close()
            assert True
        else:        
            self.driver.save_screenshot(".\\Screenshots\\" + "test_userLogin.png")
            self.driver.close()
            assert False
        