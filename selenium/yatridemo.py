import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By


class BaseTest:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.yatra.com/")
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

class TestLoginPage(BaseTest):
    def test_login(self):
        print("directed to website")
        loginblock = self.driver.find_element(By.ID, "userLoginBlock")

        # loginblock.click()
        # print("loginblock clicked")

        actions = ActionChains(self.driver)
        actions.move_to_element(loginblock).perform()

        signupbtn = self.driver.find_element(By.XPATH, "//*[@id='SignUpBtn']")
        signupbtn.click()
        print("signup clicked")

        useremail = self.driver.find_element(By.ID, "login-input")
        useremail.send_keys("tdemo0517@gmail.com")

        signupcont = self.driver.find_element(By.ID, "login-continue-btn")
        signupcont.click()
        print("signup continue")

        time.sleep(10)

        userpassword = self.driver.find_element(By.ID, "login-password")
        userpassword.send_keys("4321!@#0")

        time.sleep(10)

        loginbtn = self.driver.find_element(By.ID, "login-submit-btn")
        loginbtn.click()
        print("signup finished")

        time.sleep(10)


