from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_dropdown():
    # Inicialización del navegador
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")
    time.sleep(10)

    try:
        dropdown = driver.find_element(By.ID, "dropdown")

        # Caso 1: Seleccionar una opción 1 válida
        option1 = dropdown.find_element(By.XPATH, "//option[text()='Option 1']")
        option1.click()
        selected_option = dropdown.find_element(By.XPATH, "//option[@selected='selected']")
        assert selected_option.text == "Option 1"
        time.sleep(10)

        # Caso 2: Intentar seleccionar una opción2
        option2 = dropdown.find_element(By.XPATH, "//option[text()='Option 2']")
        option2.click()
        selected_option = dropdown.find_element(By.XPATH, "//option[@selected='selected']")
        assert selected_option.text == "Option 2"
        time.sleep(10)

        print("Pruebas de dropdown completadas.")

    finally:
        # Cierre del navegador
        driver.quit()