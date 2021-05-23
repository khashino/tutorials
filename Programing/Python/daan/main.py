from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class AzadDaanAutomation():

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password


    def setUp(self):
        options = webdriver.ChromeOptions()

        options.add_experimental_option("prefs", { \
            "profile.default_content_setting_values.media_stream_mic": 1,  # 1:allow, 2:block
        })

        self.driver = webdriver.Chrome(options=options)

    def logIn(self):
        driver = self.driver
        driver.get("http://azad.daan.ir/")

        beflogin = driver.find_element_by_class_name("btn-primary")
        beflogin.click()

        userElem = driver.find_element_by_id("identificationNumber")
        userElem.send_keys(self.username)

        passElem = driver.find_element_by_id("password")
        passElem.send_keys(self.password)
        passElem.send_keys(Keys.ENTER)

        time.sleep(1)

        btnClose = driver.find_element_by_class_name("close")
        btnClose.click()

    def findMyClass(self):
        driver = self.driver
        driver.get("http://azad.daan.ir/session-list#session-list")

        onlineCls = driver.find_element_by_link_text("ورود دانشجو")
        onlineCls.click()

        time.sleep(5)

        inputTxt = driver.find_element_by_id("message-input")
        inputTxt.send_keys("سلام استاد")
        inputTxt.send_keys(Keys.ENTER)











if __name__ == "__main__":
    myapp = AzadDaanAutomation("http://azad.daan.ir/", "14195112137321111", "test")
    myapp.setUp()
    myapp.logIn()
    myapp.findMyClass()
