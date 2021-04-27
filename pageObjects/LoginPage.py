from selenium import webdriver


class LoginPage:
    test_username_id = "Email"
    test_password_id = "Password"
    button_login_tag_name = "button"
    link_logout_linkText = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, userName):
        self.driver.find_element_by_id(self.test_username_id).clear()
        self.driver.find_element_by_id(self.test_username_id).send_keys(userName)

    def setPassword(self, userName):
        self.driver.find_element_by_id(self.test_password_id).clear()
        self.driver.find_element_by_id(self.test_password_id).send_keys(userName)

    def clickLogin(self):
        self.driver.find_element_by_tag_name(self.button_login_tag_name).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linkText).click()
