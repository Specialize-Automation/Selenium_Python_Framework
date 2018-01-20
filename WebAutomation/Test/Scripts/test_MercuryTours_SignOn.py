__author__ = 'Aditya Roy'

import unittest
from time import sleep
from WebAutomation.Src.PageObject.Pages.SignOnPage import SignOn
from WebAutomation.Src.TestBase.EnvironmentSetUp import EnvironmentSetup
from WebAutomation.Src.PageObject.Pages.HomePage import Home
from WebAutomation.Test.TestUtility.ScreenShot import SS


class MercuryTours_SignOn(EnvironmentSetup):
    def test_SignOnPage(self):

# Screenshots relative paths
        ss_path = "/Test_MercuryTours_SignOn/"

        driver = self.driver
        self.driver.get("http://newtours.demoaut.com/")
        self.driver.set_page_load_timeout(20)
# Creating object of SS screenshots utility
        ss = SS(driver)

        home = Home(driver)
        home.sign_on.click()
        sleep(2)

        if driver.title == "Sign-on: Mercury Tours":
            print("Sign On page loaded successfully")
            ss.ScreenShot(ss_path+"SignOn.png")
        else:
            print("SignOn page failed to load")

        login = SignOn(driver)
        try:
            print(login.welcomeText.get_attribute("innerText"))
            if login.registrationLink.text.find("registration"):
                print("Registration link :"+login.registrationLink.get_attribute("href"))

            print("Provide invalid username")
            login.userName.send_keys("Invalid")
            print("Provide invalid password")
            login.password.send_keys("Invalid")
            ss.ScreenShot(ss_path+"InvalidID.png")
            sleep(2)
            login.login.click()
            sleep(2)
            if driver.title == "Sign-on: Mercury Tours":
                print("Invalid Credentials Provided")
                ss.ScreenShot(ss_path + "LoginDeny.png")
        except Exception as e:
            print("Exception occurred "+e)




if __name__ == '__main__':
    unittest.main()
