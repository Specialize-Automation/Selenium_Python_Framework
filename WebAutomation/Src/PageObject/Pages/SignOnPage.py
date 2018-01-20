__author__ = 'Aditya Roy'


from selenium.webdriver.common.by import By
from WebAutomation.Src.PageObject.Locators import Locator


class SignOn(object):

# __init__(self, driver) is like constructor, to initialize the class object or instance of class
#  whenever will call this Class, this will get call and we need to pass the driver
    def __init__(self, driver):
        self.driver = driver

# home page locators defining
        self.userName = driver.find_element(By.XPATH, Locator.signOn_userName)
        self.password = driver.find_element(By.XPATH, Locator.signOn_password)
        self.login = driver.find_element(By.XPATH, Locator.signOn_login)
        self.welcomeText = driver.find_element(By.XPATH, Locator.signOn_txt)
        self.registrationLink = driver.find_element(By.XPATH,Locator.signOn_registerLink)



