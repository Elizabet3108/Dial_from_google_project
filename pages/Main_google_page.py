from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class Main_google_page:
    def __init__(self, driver):
        self.driver = driver
        self.search_line = "q"

    def search_text(self, text):
        """Entering text to search for it"""
        search_line_element = self.driver.find_element(By.NAME, self.search_line)
        search_line_element.send_keys(text)
        search_line_element.send_keys(Keys.ENTER)



