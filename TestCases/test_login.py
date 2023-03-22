#git@github.com:PoojaTayade/nopcommerceApplication.git -->My Remote Repository

import pytest
from selenium import webdriver
from PageObjectModel.LoginPage import Loginpage
from Utilities.readProperties import readConfig
from Utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = readConfig.getApplicationURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup): #driver=setup
        self.logger.info("####Test_001_Login#####")
        self.logger.info("####Test Case Started####")
        self.driver = setup #we have to launch browser here
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
           assert True
           self.driver.close()
           self.logger.info("####Test Case is Passed####")
        else:
           self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
           self.driver.close()
           self.logger.error("####Test Case is Failed####")
           assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup): #driver=setup
        self.logger.info("####Verifying Test Case####")
        self.driver = setup #we have to again launch browser here--> so we have to use fixture for that -->we write common data into a fixture-->conftest file we make in tset cases folder
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
           assert True
           self.driver.close()
           self.logger.info("####Test Case id Passed####")
        else:
           self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
           self.driver.close()
           self.logger.error("####Test Case is Failed####")
           assert False