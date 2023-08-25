from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Caso de Prueba 3: inputs is number valid
def test_by_inputs_Number():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/inputs")
    #driver.find_element(By.CLASS_NAME, "large-6 small-12 columns large-centered").send_keys(12)
    driver.find_element(By.XPATH, "//input[contains(@type,'number')]").send_keys(12)
    time.sleep(10)

    # Caso de Prueba 4: inputs is number invalid
def test_by_inputs_Number_invalid():
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/inputs")
        # driver.find_element(By.CLASS_NAME, "large-6 small-12 columns large-centered").send_keys(12)
        driver.find_element(By.XPATH, "//input[contains(@type,'number')]").send_keys("juan")
        time.sleep(10)