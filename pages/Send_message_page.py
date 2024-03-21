import re
import appium
from appium.webdriver.common.appiumby import AppiumBy


class Send_message_page:
    def __init__(self, driver: appium.webdriver):
        self.driver = driver
        self.text = "com.google.android.apps.messaging:id/compose_message_text"
        self.send = "Send SMS"
        self.number = "com.google.android.apps.messaging:id/conversation_title"
        self.message = "com.google.android.apps.messaging:id/message_text"
        self.option = "More conversation options"
        self.delete = "//*[@text='Delete']"
        self.confirm = "android:id/button1"

    def send_text_to_message(self, text):
        """Entering the text to be sent"""
        send_text = self.driver.find_element(by=AppiumBy.ID, value=self.text)
        send_text.send_keys(text)

    def click_on_send(self):
        """Click on send button"""
        sms = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=self.send)
        sms.click()

    def displayed_phone_number(self):
        """Returns the displayed phone number"""
        number = self.driver.find_element(by=AppiumBy.ID, value=self.number)
        return number.text

    def sent_message(self):
        """Returns the text of the message that was sent"""
        sent = self.driver.find_element(by=AppiumBy.ID, value=self.message)
        return sent.text

    def click_on_option(self):
        """Open a pop-up window with option"""
        pop_up = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=self.option)
        pop_up.click()

    def click_on_delete(self):
        """Click on the delete option from pop-up"""
        delete = self.driver.find_element(by=AppiumBy.XPATH, value=self.delete)
        delete.click()

    def confirmation_of_deletion(self):
        """Click on delete for confirmation"""
        button = self.driver.find_element(by=AppiumBy.ID, value=self.confirm)
        button.click()

