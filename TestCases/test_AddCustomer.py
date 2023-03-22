import random
import string

import pytest
from selenium.webdriver.common.by import By

from PageObjectModel.AddCustomerPage import AddCustomer
from PageObjectModel.LoginPage import Loginpage
from Utilities.customLogger import LogGen
from Utilities.readProperties import readConfig


class Test_003_AddCustomer:
    baseURL = readConfig.getApplicationURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup): #driver=setup
        self.logger.info("#### TestCase_003 Started ####")
        self.driver = setup #we have to launch browser here
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("#### Login Successful ####")

        self.logger.info("#### Starting AddCustomer Test ####")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddNew()

        self.logger.info("#### Providing Customer Information ####")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("vs1420")
        self.addcust.setCustomerRoles("Registered")
        self.addcust.setFirstName("Pooja")
        self.addcust.setLastName("Tayade")
        self.addcust.setGender("Female")
        self.addcust.setDOB("10/20/1992")
        self.addcust.setCompanyName("GetGate")
        self.addcust.setManagerOfVendor("Vendor 1")
        self.addcust.setAdminContent("This is for testing ")
        self.addcust.clickOnSave()

        self.logger.info("#### saving Customer Information ####")

        self.logger.info("#### Adding Customer Validations ####")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if "customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("#### Add Customer Test Passed ####")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png") #saving screenshot
            self.logger.error("#### Add Customer Test Failed ####")
            assert True == False

        self.driver.close()
        self.logger.info("#### Ending Add Customer Test ####")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))












