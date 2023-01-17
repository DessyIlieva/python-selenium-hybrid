from pageObjects.LoginPage import LoginPage
from pageObjects.NavigationLinks import NavMenu
from pageObjects.CreateUserPage import CreateUser
from pageObjects.UserProfilePage import UserProfile
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import pytest

class Test_002_User_Create:
    baseURL = ReadConfig.getApplicationURL()
    path = './/TestData/createUserData.xlsx'  
    logger = LogGen.loggen()
    img = "\\testCases\\user\\userImage.png"

    @pytest.mark.regression
    def test_userCreateAndDelete(self, setup):
        self.logger.info("########## Verifying User Creation ##########")
        self.driver = setup            
        self.driver.get(self.baseURL)
        self.navMenu = NavMenu(self.driver)
        self.loginPage=LoginPage(self.driver)
        self.createPage = CreateUser(self.driver)
        self.profilePage = UserProfile(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        iterationStatus = []
        self.driver.implicitly_wait(3)


        for row in range (2, self.rows+1):
            self.logger.info("########## Getting Data ##########")
            self.usernameData = XLUtils.readData(self.path, 'Sheet1', row, 1)
            self.emailData = XLUtils.readData(self.path, 'Sheet1', row, 2)
            self.passwordData = XLUtils.readData(self.path, 'Sheet1', row, 3)
            self.descriptionData = XLUtils.readData(self.path, 'Sheet1', row, 4)

            self.logger.info("########## Executing Sign Up Steps ##########")
            self.navMenu.signUpPage()
            self.createPage.setUsername(self.usernameData)
            self.createPage.setEmail(self.emailData)
            self.createPage.setPassword(self.passwordData)
            self.createPage.uploadPicture(self.img)
            self.createPage.setDescription(self.descriptionData)
            self.createPage.clickSignUp()

            self.logger.info("########## Executing Log In and View Profile Steps ##########")
            self.loginPage.setUsername(self.usernameData)
            self.loginPage.setPassword(self.passwordData)
            self.loginPage.clickLogin()
            self.navMenu.viewProfilePage()

            self.logger.info("########## Verifying Account Details ##########")
            if (self.usernameData == self.profilePage.getUsername()
                    and "userImage" in self.profilePage.getImageTitle()
                    and self.descriptionData == self.profilePage.getUserDescription()):
                iterationStatus.append('Success')
                self.logger.info("########## New User Details Match ##########")
            else:
                iterationStatus.append('Failure')
                self.driver.save_screenshot(".\\Screenshots\\" + "test_UserCreate.png")
                self.logger.error("########## New User Details Do NOT Match ##########")

            self.logger.info("########## Executing Delete Account Steps ##########")
            self.navMenu.deleteAccountPage()
            self.profilePage.clickConfirmDelete()

            if not self.navMenu.addBookButtonPresent():
                iterationStatus.append('Success')
                self.logger.info("########## User Deleted and Logged Out Successfully ##########")
            else:
                iterationStatus.append('Failure')
                self.driver.save_screenshot(".\\Screenshots\\" + "test_UserDelete.png")
                self.logger.error("########## User Deletion Issue ##########")

        if "Failure" not in iterationStatus:
            self.logger.info("########## User Creation and Deletion Test Passed Successfully ##########")
            assert True
        else:
            self.logger.error("########## User Creation and Deletion Test Failed ##########")
            self.logger.error(iterationStatus)
            assert False