from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


#Caso de prueba 4: hover information
def test_hover_diplay_information():
            # Inicialización del navegador
            driver = webdriver.Chrome()
            driver.get("https://the-internet.herokuapp.com/hovers")
            time.sleep(20)

            try:
                # Encuentra todas las imágenes
                figures = driver.find_elements(By.CLASS_NAME, "figure")

                # Itera sobre cada figura y realiza el hover
                for figure in figures:
                    hover = ActionChains(driver).move_to_element(figure)
                    hover.perform()
                    time.sleep(4)  # Espera para que la información del hover aparezca

                    #view_profile_link = figcaption.find_element(By.XPATH, "/a[@href='/users/1'][contains(.,'View profile')]")
                    #view_profile_link.click()

                    # Obtiene la información del hover
                    figcaption = figure.find_element(By.CLASS_NAME, "figcaption")
                    print(figcaption.text)

            finally:
                # Cierre del navegador
                driver.quit()

#Caso de prueba 5: Click View information not found
def test_links_to_not_found():
    # Inicialización del navegador
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/hovers")
    time.sleep(10)

    try:

        # Encuentra todas las imágenes
        figures = driver.find_elements(By.CLASS_NAME, "figure")

        # Variable para controlar si se encontró la página "Not Found"
        found_not_found = False

        # Itera sobre cada figura y realiza clic en el enlace "View profile"
        for figure in figures:
            hover = ActionChains(driver).move_to_element(figure)
            hover.perform()
            view_profile_link = figure.find_element(By.XPATH, "(//a[contains(.,'View profile')])[1]")
            view_profile_link.click()
            time.sleep(4)

            # Espera a que la página "not found" se cargue
            time.sleep(15)  # Aumenta el tiempo de espera

            # Verifica si la página de "not found" se ha cargado
            try:
                not_found_message = driver.find_element(By.XPATH, "//h1[contains(text(), 'Not Found')]")
                if not_found_message.text == "Not Found":
                    print("Página 'Not Found' encontrada. Test finalizado.")
                    found_not_found = True
                    break
            except:
                pass  # Continúa con el siguiente enlace si no se encontró el mensaje

            # Regresa a la página anterior
            driver.back()

        if not found_not_found:
            print("Página 'Not Found' no encontrada. Test finalizado sin encontrarla.")

    finally:
        # Cierre del navegador
        driver.quit()
