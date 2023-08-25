from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = "username"
        self.password_textbox_id = "password"
        self.login_button_id = "//i[@class='fa fa-2x fa-sign-in'][contains(.,'Login')]"

    def test_enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def test_enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def test_click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_id).click()


