from selenium import webdriver

from selenium.webdriver.common.keys import Keys

class AzadDaanAutomation():

    def __init__(self,url,username,password):
        self.url = url
        self.username = username
        self.password = password

    def setUp(self):
        self.driver = webdriver.Chrome()

    def logIn(self):
        driver = self.driver
        driver.get(self.url)

        warning = driver.find_element_by_class_name("btn-warning")
        warning.click()

        loginElem = driver.find_element_by_name("identification_number")
        loginElem.send_keys(self.username)

        passElem = driver.find_element_by_name("password")
        passElem.send_keys(self.password)

        submitBtn = driver.find_element_by_class_name("btn-primary")
        submitBtn.click()




if __name__ == "__main__":
    myapp = AzadDaanAutomation("http://azad.daan.ir/","14195112137321111","")
    myapp.setUp()
    myapp.logIn()

