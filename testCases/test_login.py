import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):

        self.logger.info("***************** Test_001_Login *****************")
        self.logger.info("************** Verifying Home Page Title ************** ")

        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("***************** Home Page Title test is passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("***************** Home Page Title test is failed *****************")
            assert False

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("************** Verifying Login Test ************** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("***************** Login test is passed *****************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("***************** Login test is failed *****************")
            assert False
