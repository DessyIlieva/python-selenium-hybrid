from pageObjects.LoginPage import LoginPage
from pageObjects.NavigationLinks import NavMenu
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import pytest

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = './/TestData/loginData.xlsx'
    logger = LogGen.loggen()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_userLoggedOut(self, setup):
        self.logger.info("########## Verifying User is Logged Out ##########")
        self.driver = setup            
        self.driver.get(self.baseURL)
        self.navMenu = NavMenu(self.driver)
        self.loginPage=LoginPage(self.driver)
        

        # Verify Add Book button is NOT visible
        if not self.navMenu.addBookButtonPresent():
            self.logger.info("########## User is Logged Out Test Passed Successfully ##########")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_userLoggedOut.png")
            self.logger.error("########## User is Logged Out Test Failed ##########")
            assert False

    @pytest.mark.regression
    def test_userLoginLogout(self, setup):
        self.logger.info("########## Verifying User Login ##########")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.navMenu = NavMenu(self.driver)
        self.loginPage=LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        loginStatus = []

        for row in range(2, self.rows+1):
            # Getting data
            self.usernameData = XLUtils.readData(self.path, 'Sheet1', row, 1)
            self.passwordData = XLUtils.readData(self.path, 'Sheet1', row, 2)
            self.expected = XLUtils.readData(self.path, 'Sheet1', row, 3)

            # Executing Steps
            self.navMenu.loginPage()
            self.loginPage.setUsername(self.usernameData)
            self.loginPage.setPassword(self.passwordData)
            self.loginPage.clickLogin()

            # Verifying expected results
            if self.navMenu.addBookButtonPresent() and self.expected == 'Pass':
                loginStatus.append('Success')
                self.navMenu.clickLogout()
            elif self.navMenu.addBookButtonPresent() and self.expected == 'Fail':
                loginStatus.append('Failure')
                self.navMenu.clickLogout()
            elif not self.navMenu.addBookButtonPresent() and self.expected == 'Fail':
                loginStatus.append('Success')
            elif not self.navMenu.addBookButtonPresent() and self.expected == 'Pass':
                loginStatus.append('Failure')

        if "Failure" not in loginStatus:
            self.logger.info("########## User Login Test Passed Successfully ##########")
            assert True
        else:
            self.logger.error("########## User Login Test Failed ##########")
            assert False