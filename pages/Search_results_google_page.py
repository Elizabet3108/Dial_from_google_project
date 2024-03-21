from selenium.webdriver.common.by import By


class Search_results_page:
    def __init__(self, driver):
        self.driver = driver
        self.phone_number = "span.LrzXr.zdqRlf.kno-fv"
        self.open = "//*[@class='JjSWRd']/span[1]/span/span"

    def get_phone_number(self):
        """Getting a phone number from a finding page"""
        phone_number_element = self.driver.find_element(By.CSS_SELECTOR, self.phone_number)
        number = phone_number_element.text
        return number.replace("-", "")
