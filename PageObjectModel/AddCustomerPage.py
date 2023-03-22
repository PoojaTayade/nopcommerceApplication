import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    #Add Customer Page
    lnkCustomer_menu_link_text = "Customers"
    lnkCustomer_menuitem_xpath = "//a[@href ='/Admin/Customer/List']"
    btn_Add_NewCustomer_xpath = "//a[@href = '/Admin/Customer/Create']"
    txt_email_xpath = "//input[@id = 'Email']"
    txt_password_xpath = "//input[@id = 'Password']"
    txt_FirstName_xpath = "//input[@id = 'FirstName']"
    txt_LastName_xpath = "//input[@id = 'LastName']"
    rd_Male_Gendar_xpath = "//input[@id = 'Gender_Male']"
    rd_Female_Gender_xpath = "//input[@id = 'Gender_Female']"
    txt_DOB_xpath = "//input[@id = 'DateOfBirth']"
    txt_CompanyName_xpath = "//input[@id = 'Company']"
    txt_CustomerRoles_xpath = "//*[@id='SelectedCustomerRoleIds_label']"
    lstIitem_Adinstrator_xpath = "//li[text()='Administrators']"
    lstIitem_ForumModerators_xpath = "//li[text()='Forum Moderators']"
    lstIitem_Guests_xpath = "//li[text()='Guests']"
    lstIitem_Registered_xpath = "//li[text()='Registered']"
    lstIitem_Vendors_xpath = "//li[text()='Vendors']"
    txt_MgrVendors_xpath = "//select[@id = 'VendorId']"
    txt_AdminComment_xpath = "//*[@id = 'AdminComment']"
    btn_Save_xpath = "//button[@name = 'save']"

    # Checkbox1_xpath = "//input[@id = 'IsTaxExempt']"
    # Checkbox2_xpath = "//input[@id = 'Active']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.LINK_TEXT, self.lnkCustomer_menu_link_text).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btn_Add_NewCustomer_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH, self.txt_CustomerRoles_xpath).click()
        time.sleep(5)
        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lstIitem_Registered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstIitem_Adinstrator_xpath)
        elif role == "Guests":
            #Here user can be Registered or Guest only one
            time.sleep(3)
            self.listitem = self.driver.find_element(By.XPATH, "//li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstIitem_Guests_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.lstIitem_Vendors_xpath)
        elif role == "ForumModerators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstIitem_ForumModerators_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstIitem_Guests_xpath)
            #self.listitem.click() #--> is not working then we use following javascript method for click action
            time.sleep(3)
            #self.listitem.click();
            self.driver.execute_script("arguments[0].click();", self.listitem)

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH, self.txt_FirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH, self.txt_LastName_xpath).send_keys(lname)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.rd_Male_Gendar_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.rd_Female_Gender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rd_Female_Gender_xpath).click()

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.txt_DOB_xpath).send_keys(dob)

    def setCompanyName(self, cmpname):
        self.driver.find_element(By.XPATH, self.txt_CompanyName_xpath).send_keys(cmpname)

    def setManagerOfVendor(self,value):
        drp = Select(self.driver.find_element(By.XPATH, self.txt_MgrVendors_xpath))
        drp.select_by_visible_text(value)

    def setAdminContent(self,content):
        self.driver.find_element(By.XPATH, self.txt_AdminComment_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btn_Save_xpath).click()







