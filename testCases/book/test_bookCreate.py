from pageObjects.LoginPage import LoginPage
from pageObjects.NavigationLinks import NavMenu
from pageObjects.UserProfilePage import UserProfile
from pageObjects.AddBookPage import AddBook
from pageObjects.BookDetailsPage import BookDetails
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import pytest


class Test_003_AddBook:
    baseURL = ReadConfig.getApplicationURL()
    usernameData = ReadConfig.getUsername()
    passwordData = ReadConfig.getPassword()
    path = './/TestData/createBookData.xlsx'  
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_bookCreateAndDelete(self, setup):
        self.logger.info("########## Verifying Book Creation ##########")
        self.driver = setup            
        self.driver.get(self.baseURL)
        self.navMenu = NavMenu(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.addBookPage = AddBook(self.driver)
        self.profilePage = UserProfile(self.driver)
        self.bookDetailsPage = BookDetails(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        iterationStatus = []
        self.driver.implicitly_wait(3)


        for row in range (2, self.rows+1):
            self.logger.info("########## Getting Data ##########")
            self.titleData = XLUtils.readData(self.path, 'Sheet1', row, 1)
            self.authorData = XLUtils.readData(self.path, 'Sheet1', row, 2)
            self.giveAwayData = XLUtils.readData(self.path, 'Sheet1', row, 3)
            self.exchangeData = XLUtils.readData(self.path, 'Sheet1', row, 4)
            self.languageData = XLUtils.readData(self.path, 'Sheet1', row, 5)
            self.genreData = XLUtils.readData(self.path, 'Sheet1', row, 6)
            self.descriptionData = XLUtils.readData(self.path, 'Sheet1', row, 7)

            self.logger.info("########## Executing Log In Steps ##########")
            self.navMenu.loginPage()
            self.loginPage.setUsername(self.usernameData)
            self.loginPage.setPassword(self.passwordData)
            self.loginPage.clickLogin()
            

            self.logger.info("########## Executing Create Book Steps ##########")
            self.navMenu.clickAddBook()
            self.addBookPage.setTitle(self.titleData)
            self.addBookPage.setAuthor(self.authorData)
            self.addBookPage.setGiveAway(self.giveAwayData)
            self.addBookPage.setExchange(self.exchangeData)
            self.addBookPage.setLanguage(self.languageData)
            self.addBookPage.setGenre(self.genreData)
            self.addBookPage.setDescription(self.descriptionData)
            self.addBookPage.clickSubmit()

            self.logger.info("########## Verify New Book Details Match ##########")
            self.navMenu.viewProfilePage()
            self.profilePage.clickBookCardByTitle(self.titleData)

            #Verify Author
            if self.authorData in self.bookDetailsPage.getAuthor():
                iterationStatus.append('Success')
            else:
                iterationStatus.append('Failure')
            # Verify language
            if self.languageData == self.bookDetailsPage.getLanguage():
                iterationStatus.append('Success')
            else:
                iterationStatus.append('Failure')
            # Verify genre
            if self.genreData == self.bookDetailsPage.getGenre():
                iterationStatus.append('Success')
            else:
                iterationStatus.append('Failure')
            # Verify givingAway
            if self.giveAwayData == self.bookDetailsPage.getGivingAway():
                iterationStatus.append('Success')
            else:
                iterationStatus.append('Failure')
            # Verify exchanging
            if self.exchangeData == self.bookDetailsPage.getExchanging():
                iterationStatus.append('Success')
            else:
                iterationStatus.append('Failure')
            # Verify description
            if self.descriptionData == self.bookDetailsPage.getDescription():
                iterationStatus.append('Success')
            else:
                iterationStatus.append('Failure')
          

            self.logger.info("########## Executing Delete Book Steps ##########")
            self.bookDetailsPage.clickDelete()
            self.bookDetailsPage.clickConfirmDelete()

            self.logger.info("########## Verify Book Deleted Successfully ##########")
            self.navMenu.viewProfilePage()
            if self.titleData not in self.profilePage.getBookTitles():
                iterationStatus.append('Success')
                self.logger.info("########## Book Deleted Successfully ##########")
            else:
                iterationStatus.append('Failure')
                self.driver.save_screenshot(".\\Screenshots\\" + "test_bookDelete.png")
                self.logger.error("########## Book NOT Deleted ##########")

        if "Failure" not in iterationStatus:
            self.logger.info("########## Book Creation and Deletion Test Passed Successfully ##########")
            assert True
        else:
            self.logger.error("########## Book Creation and Deletion Test Failed ##########")
            self.logger.error(iterationStatus)
            assert False