from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pages.loginPage import (LoginPage)
from pages.homePage import HomePage

#Caso de Prueba 1: Inicio de Sesión Válido
def test_element_by_id():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    login = LoginPage(driver)
    time.sleep(10)
    #home = HomePage(driver)
    login.test_enter_username("tomsmith")
    login.test_enter_password("SuperSecretPassword!")
    login.test_click_login()
    time.sleep(15)

    homepage = HomePage(driver)
    homepage.test_click_logout()
    time.sleep(15)

    #driver.find_element(By.ID, "username").send_keys("tomsmith")
    #driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    #driver.find_element(By.XPATH, "//i[@class='fa fa-2x fa-sign-in'][contains(.,'Login')]").click()
    time.sleep(8)
   # driver.find_element(By.XPATH, "//i[contains(.,'Logout')]").click()
    time.sleep(5)

# Caso de Prueba 2: Inicio de Sesión Inválido
def test_by_wrong_credentials():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    login = LoginPage(driver)
    time.sleep(10)
    # home = HomePage(driver)
    login.test_enter_username("smithtom")
    login.test_enter_password("SecretPassword!Super")
    login.test_click_login()
    time.sleep(15)
    #driver.get("https://the-internet.herokuapp.com/login")
    #driver.find_element(By.ID, "username").send_keys("smithtom")
    #driver.find_element(By.ID, "password").send_keys("SecretPassword!Super")
    #driver.find_element(By.XPATH, "//i[@class='fa fa-2x fa-sign-in'][contains(.,'Login')]").click()
