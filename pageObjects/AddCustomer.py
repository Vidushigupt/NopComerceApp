from selenium import webdriver
import time

from selenium.webdriver.support.select import Select


class AddCustomerPage:
    linkCustomer_main_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p/text()"
    linkCustomer_sub_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    btnAddNew_link_text="/Admin/Customer/Create"

    txtEmail_id = "Email"
    txtPassword_id = "Password"
    txtFirstName_id = "FirstName"
    txtLastName_id = "LastName"
    rdGenderMale_id = "Gender_Male"
    rdGenderFemale_id = "Gender_Female"
    txtDOB_id = "DateOfBirth"
    txtCompanyName_id = "Company"
    chkIsTaxExempt_id = "IsTaxExempt"

    txtNewsletter_xpath = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    lstTestStore2_xpath = "//*[@id='eca6d22a-80a2-4e18-8886-cdb4723333f4']"
    lstYourStoreName_xpath = "//*[@id='eca6d22a-80a2-4e18-8886-cdb4723333f4']"

    txtCostumerRoles_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lstAdministrators_xpath = "//*[@id='950e8a49-18a7-49db-8a4f-4ecf98569c7a']"
    lstForumModerators_xpath = "//*[@id='950e8a49-18a7-49db-8a4f-4ecf98569c7a']"
    lstGuests_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    lstRegistered_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[4]"
    lstVendors_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[5]"

    drpManagerOfVendors_xpath = "//*[@id='VendorId']"
    chkActive_xpath = "//*[@id='Active']"
    txtAdminContent_xpath = "//*[@id='AdminComment']"

    btnSave_name = "save"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMainMenu(self):
        self.driver.find_element_by_xpath(self.linkCustomer_main_menu_xpath).click()

    def clickOnCustomerSubMenu(self):
        self.driver.find_element_by_xpath(self.linkCustomer_sub_menu_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_link_text(self.btnAddNew_link_text).click()

    def setEmail(self, email):
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.txtPassword_id).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(lname)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element_by_id(self.rdGenderMale_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.rdGenderFemale_id).click()
        else:
            self.driver.find_element_by_id(self.rdGenderMale_id).click()

    def setDob(self, dob):
        self.driver.find_eleme/nt_by_id(self.txtDOB_id).send_keys(dob)

    def setCompanyName(self, companyName):
        self.driver.find_element_by_id(self.txtCompanyName_id).send_keys(companyName)

    def setIsTaxExempt(self, IsTaxExempt):
        self.isTaxExemptIsEnabled = self.driver.find_element_by_id(self.chkIsTaxExempt_id).isSelected()
        if IsTaxExempt == "Yes":
            if self.isTaxExemptIsEnabled == "False":
                self.driver.find_element_by_id(self.chkIsTaxExempt_id).click()

        elif IsTaxExempt == "No":
            if self.isTaxExemptIsEnabled == "True":
                self.driver.find_element_by_id(self.chkIsTaxExempt_id).click()

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtCostumerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstRegistered_xpath)
        elif role=='Administrators':
            self.listitem=self.driver.find_element_by_xpath(self.lstAdministrators_xpath)
        elif role=='Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstGuests_xpath)
        elif role=='Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstRegistered_xpath)
        elif role=='Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lstVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpManagerOfVendors_xpath))
        drp.select_by_visible_text(value)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_name).click()
