from selenium.webdriver.common.by import By


class SearchCustomer:

    txt_Email_xpath = "//input[@id = 'SearchEmail']"
    txt_FirstName_xpath = "//input[@id = 'SearchFirstName']"
    txt_LastName_xpath = "//input[@id = 'SearchLastName']"
    btn_Search_xpath = "//button[@id = 'search-customers']"

    table_xpath = "//div[@class = 'dataTables_scrollBody']"
    table_Rows_xpath = "//table[@id = 'customers-grid']//tbody/tr"
    table_Columns_xpath = "//table[@id = 'customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txt_Email_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_Email_xpath).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH, self.txt_FirstName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_FirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH, self.txt_LastName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_LastName_xpath).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.btn_Search_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_Rows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.table_Columns_xpath))

    def searchCustomerByEmail(self,email):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id = 'customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self,Name):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)                      #Row No   #Column No
            name = table.find_element(By.XPATH, "//table[@id = 'customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag

