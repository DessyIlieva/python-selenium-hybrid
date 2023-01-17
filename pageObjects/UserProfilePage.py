from selenium.webdriver.common.by import By

class UserProfile():

    confirmDeleteAccountButton = (By.XPATH, '//input[@value="Confirm"]')
    usernameText = (By.XPATH, '//h2[@class="userName"]')
    descriptionText = (By.XPATH, '//p[@class="userDescription"]') 
    imgTitle = (By.XPATH, "//img[@height=150]")
    userBookCards = (By.CSS_SELECTOR, '.h-100')
    cardTitle = (By.CLASS_NAME, 'card-title')

    def __init__(self,driver):
        self.driver=driver

    def clickConfirmDelete(self):
        deleteAccount = self.driver.find_element(*self.confirmDeleteAccountButton)
        deleteAccount.click()


    def getUsername(self):
        element = self.driver.find_element(*self.usernameText)
        username = element.text
        return username


    def getUserDescription(self):
        element = self.driver.find_element(*self.descriptionText)
        description = element.text
        return description


    def getImageTitle(self):
        element = self.driver.find_element(*self.imgTitle)
        title = element.get_attribute("src")
        return title


    def clickBookCardByTitle(self, titleData):
        books = self.driver.find_elements(*self.userBookCards)
        for _ in books:
            title = self.driver.find_element(*self.cardTitle)
            titleText = title.text
            if titleText == titleData:
                title.click()
                break

    def getBookTitles(self):
        books = self.driver.find_elements(*self.userBookCards)
        booksTitles = []
        for _ in books:
            title = self.driver.find_element(*self.cardTitle).text
            booksTitles.append(title)
        return booksTitles
    