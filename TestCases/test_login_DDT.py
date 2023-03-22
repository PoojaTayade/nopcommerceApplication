import time
import openpyxl
import pytest
from selenium import webdriver
from PageObjectModel.LoginPage import Loginpage
from Utilities.readProperties import readConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = readConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("**** Test_002_DDT_login ****")
        self.logger.info("**** Verfying login DDT test ****")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Loginpage(self.driver)

        self.rows = XLUtils.getRowCount(self.path,"Sheet1")
        print("No. of rows in a Excel:",self.rows)

        lst_status = []  #empty list variable

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path,"Sheet1", r,2)
            self.exp = XLUtils.readData(self.path,"Sheet1",r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"


            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("**** Passed ****")
                    self.lp.clicklogout();
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("**** Failed ****")
                    self.lp.clicklogout();
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("**** Failed ****")
                    lst_status.append("Fail")

                elif self.exp == "Fail":
                    self.logger.info("**** Paseed ****")
                    lst_status.append("Pass")


        if "Fail" not in lst_status:
            self.logger.info("****  Login DDT test passed ****")
            self.driver.close()
            assert True

        else:
            self.logger.info("****  Login DDT test failed ****")
            self.driver.close()
            assert False


        self.logger.info("**** End of DDT test ****")
        self.logger.info("**** TC_002 Completed ****")







        



















