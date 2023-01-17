from selenium.webdriver.common.by import By

class NavMenu():
    userDropdownButton = (By.XPATH, "//a[@role='button']")
    loginPageButton = (By.LINK_TEXT, "Log In")
    logOutButton = (By.LINK_TEXT, 'Log Out')
    signUpPageButton = (By.LINK_TEXT, 'Sign Up')
    viewProfilePageButton = (By.LINK_TEXT, 'View Profile')
    deleteAccountPageButton = (By.LINK_TEXT, 'Delete Account')
    addBookButton = (By.XPATH, "//a[.='Add Book']" )
    searchButton = (By.XPATH, '//button[text()="Search"]')
    searchField = (By.XPATH, '//input[@aria-label="Search"]')



    def __init__(self,driver):
        self.driver=driver


    def loginPage(self):
        userDropdown = self.driver.find_element(*self.userDropdownButton)
        userDropdown.click()
        login = self.driver.find_element(*self.loginPageButton)
        login.click()


    def signUpPage(self):
        userDropdown = self.driver.find_element(*self.userDropdownButton)
        userDropdown.click()
        viewProfile = self.driver.find_element(*self.signUpPageButton)
        viewProfile.click()


    def viewProfilePage(self):
        userDropdown = self.driver.find_element(*self.userDropdownButton)
        userDropdown.click()
        viewProfile = self.driver.find_element(*self.viewProfilePageButton)
        viewProfile.click()


    def clickLogout(self):
        userDropdown = self.driver.find_element(*self.userDropdownButton)
        userDropdown.click()
        logout = self.driver.find_element(*self.logOutButton)
        logout.click()    


    def deleteAccountPage(self):
        userDropdown = self.driver.find_element(*self.userDropdownButton)
        userDropdown.click()
        deleteAccount = self.driver.find_element(*self.deleteAccountPageButton)
        deleteAccount.click() 


    def clickAddBook(self):
        addbook = self.driver.find_element(*self.addBookButton)
        addbook.click()


    def setSearch(self, bookTitle):
        searchField = self.driver.find_element(*self.searchField)
        searchField.send_keys(bookTitle)


    def clickSearch(self):
        searchButton = self.driver.find_element(*self.searchButton)
        searchButton.click()


    def addBookButtonPresent(self):
        addBookPresent = False
        addBook = self.driver.find_elements(*self.addBookButton)
        if len(addBook) > 0:
            addBookPresent = True
        return addBookPresent