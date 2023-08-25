from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        #self.welcome_link_id = "Logout"
        self.logout_link_linkText = "//i[contains(.,'Logout')]"

    def test_click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_link_linkText).click()