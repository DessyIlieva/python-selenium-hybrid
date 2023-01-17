from selenium.webdriver.common.by import By
import os

class CreateUser():

    usernameField = (By.ID, 'username')
    emailField = (By.ID, 'id_email')
    passwordField = (By.ID, 'id_password')
    pictureField = (By.NAME, 'userImage')
    descriptionField = (By.NAME, 'userDescription')
    signUpButton = (By.XPATH, '//input[@value="Sign Up"]')
    signUpSuccessMessage = (By.CSS_SELECTOR, "[class*='alert-dismissible']")


    def __init__(self,driver):
        self.driver=driver

    def setUsername(self, usernameData):
        username = self.driver.find_element(*self.usernameField)
        username.clear()
        username.send_keys(usernameData)

    def setPassword(self, passwordData):
        password = self.driver.find_element(*self.passwordField)
        password.clear()
        password.send_keys(passwordData)

    def setEmail(self, emailData):
        email = self.driver.find_element(*self.emailField)
        email.clear()
        email.send_keys(emailData)

    def uploadPicture(self, imgPath):
        picture = self.driver.find_element(*self.pictureField)
        picture.send_keys(os.getcwd() + imgPath)

    def setDescription(self, descriptionData):
        email = self.driver.find_element(*self.descriptionField)
        email.clear()
        email.send_keys(descriptionData)

    def clickSignUp(self):
        signUp = self.driver.find_element(*self.signUpButton)
        signUp.click()
