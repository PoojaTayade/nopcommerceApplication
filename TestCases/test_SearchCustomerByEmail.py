import time

import pytest

from PageObjectModel.AddCustomerPage import AddCustomer
from PageObjectModel.LoginPage import Loginpage
from PageObjectModel.Search_Customer import SearchCustomer
from Utilities.customLogger import LogGen
from Utilities.readProperties import readConfig


class Test_004_SearchCustomerByEmail:
    baseURL = readConfig.getApplicationURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_SearchCustomer(self,setup): #driver=setup
        self.logger.info("####Test Case Started####")
        self.driver = setup #we have to launch browser here
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("#### Login Successful ####")

        self.logger.info("#### Start for Seraching Customer by Email ####")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("#### Seraching Customer by Email ####")
        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setEmail("victoria_victoria@nopCommerce.com")
        self.searchcust.clickSearch()
        time.sleep(5)
        status = self.searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status

        self.driver.close()

        self.logger.info("#### Test 004 Completed ####")









