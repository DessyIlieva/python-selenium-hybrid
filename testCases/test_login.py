from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    usernameData = ReadConfig.getUsername()
    passwordData = ReadConfig.getPassword()   
    logger = LogGen.loggen()

    
    def test_userLoggedOut(self, setup):
        self.logger.info("########## Test_001_Login ##########")
        self.logger.info("########## Verifying User is Logged Out ##########")
        self.driver = setup            
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)

        # Verify Add Book button is NOT visible
        if not self.lp.addBookButtonPresent():
            self.logger.info("########## User is Logged Out Test Passed Successfully ##########")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_userLoggedOut.png")
            self.logger.error("########## User is Logged Out Test Failed ##########")
            assert False
        

    def test_userLogin(self, setup):
        self.logger.info("########## Verifying User Login ##########")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.usernameData)
        self.lp.setPassword(self.passwordData)
        self.lp.clickLogin()

        # Verify Add Book button is visible
        if self.lp.addBookButtonPresent():
            self.logger.info("########## User Login Test Passed Successfully ##########")
            assert True
        else:        
            self.driver.save_screenshot(".\\Screenshots\\" + "test_userLogin.png")
            self.logger.error("########## User Login Test Failed ##########")
            assert False
        