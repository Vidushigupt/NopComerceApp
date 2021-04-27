import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XlUtils
import time


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"

    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("************** Test_002_DDT_Login ******************")
        self.logger.info("************** Verifying Login Test DDT ************** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XlUtils.get_row_count(self.path, "Sheet1")
        print("No of rows in excel file: ", self.rows)

        list_status = []

        for r in range(2, self.rows + 1):
            self.user = XlUtils.read_data(self.path, 'Sheet1', r, 1)
            self.password = XlUtils.read_data(self.path, 'Sheet1', r, 2)
            self.exp = XlUtils.read_data(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            time.sleep(5)

            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title == expected_title:
                if self.exp == "Pass":
                    self.logger.info("***** Passed *****")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***** Failed *****")
                    self.lp.clickLogout()
                    list_status.append("Fail")
            elif actual_title != expected_title:
                if self.exp == "Pass":
                    self.logger.info("***** Failed *****")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("***** Passed *****")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("***************** Login DDT test is Passed *****************")
            self.driver.close()
            assert True
        else:
            self.logger.info("***************** Login DDT test is Failed *****************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_ddt.png")
            self.driver.close()
            assert False
        print(list_status)
        self.logger.error("***************** End of Login DDT Test ****************")
        self.logger.error("***************** Completed Test_002_DDT_Login ****************")
