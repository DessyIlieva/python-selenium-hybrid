from selenium.webdriver.common.by import By
import time

class AddBook():
    titleField = (By.NAME, 'title')
    authorField = (By.NAME, 'author')
    giveAwayCheckbox = (By.NAME, 'giveaway')
    exchangeCheckbox = (By.NAME, 'exchange')
    languageOptions = (By.XPATH, "//div[@id='div_id_language']/div/div/label")
    genreOptions = (By.XPATH, "//div[@id='div_id_genre']/div/div/label")
    descriptionField = (By.NAME, 'description')
    submitButton = (By.XPATH, "//input[@type='submit']")


    def __init__(self,driver):
        self.driver=driver


    def setTitle(self, titleData):
        title = self.driver.find_element(*self.titleField)
        title.clear()
        title.send_keys(titleData)

    
    def setAuthor(self, authorData):
        author = self.driver.find_element(*self.authorField)
        author.clear()
        author.send_keys(authorData)


    def setGiveAway(self, giveAwayData):
        giveAway = self.driver.find_element(*self.giveAwayCheckbox)
        if giveAwayData == "True":
            giveAway.click()


    def setExchange(self, exchangeData):
        exchange = self.driver.find_element(*self.exchangeCheckbox)
        if exchangeData == "True":
            exchange.click()


    def setLanguage(self, languageData):
        languageOptions = self.driver.find_elements(*self.languageOptions)
        for languageOption in languageOptions:
            languageText = languageOption.text
            if languageText == languageData:
                languageOption.click()
                break


    def setGenre(self, genreData):
        genreOptions = self.driver.find_elements(*self.genreOptions)
        for genreOption in genreOptions:
            genreText = genreOption.text
            if genreText == genreData:
                genreOption.click()
                break


    def setDescription(self, descriptionData):
        description = self.driver.find_element(*self.descriptionField)
        description.clear()
        description.send_keys(descriptionData)


    def clickSubmit(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
        submit = self.driver.find_element(*self.submitButton)
        submit.click()