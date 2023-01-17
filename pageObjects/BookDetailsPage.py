from selenium.webdriver.common.by import By
import time

class BookDetails():
    deleteButton = (By.XPATH, '//button[text()="Delete Book"]')
    confirmDeleteButton = (By.XPATH, '//input[@value="Delete"]')
    authorText = (By.CSS_SELECTOR, 'h4')
    languageButton = (By.XPATH, "//div[@class='col-6']/div/p[1]/button")
    genreButton = (By.XPATH, "//div[@class='col-6']/div/p[2]/button")
    givingAwayButton = (By.XPATH, "//div[@class='card-body']/button[1]")
    exchangeButton = (By.XPATH, "//div[@class='card-body']/button[2]")
    descriptionText = (By.XPATH, "//div[@class='col-6']/div/p[3]")



    def __init__(self,driver):
        self.driver=driver


    def clickDelete(self):
        delete = self.driver.find_element(*self.deleteButton)
        delete.click()

    
    def clickConfirmDelete(self):
        confirmDelete = self.driver.find_element(*self.confirmDeleteButton)
        confirmDelete.click()

    
    def getAuthor(self):
        time.sleep(2)
        author = self.driver.find_element(*self.authorText).text
        return author


    def getLanguage(self):
        language = self.driver.find_element(*self.languageButton).text
        return language


    def getGenre(self):
        genres = self.driver.find_element(*self.genreButton).text
        return genres


    def getGivingAway(self):
        givingAway = self.driver.find_element(*self.givingAwayButton).get_attribute('class')
        if "success" in givingAway:
            return 'True'
        else:
            return 'False'


    def getExchanging(self):
        exchanging = self.driver.find_element(*self.exchangeButton).get_attribute('class')
        if "success" in exchanging:
            return 'True'
        else:
            return 'False'


    def getDescription(self):
        description = self.driver.find_element(*self.descriptionText).text
        return description