import re
import appium
from appium.webdriver.common.appiumby import AppiumBy


class Dial_phone_page:
    def __init__(self, driver: appium.webdriver):
        self.driver = driver
        self.dial_pad = "com.google.android.dialer:id/dialpad_fab"
        self.number_zero = "com.google.android.dialer:id/zero"
        self.number_one = "com.google.android.dialer:id/one"
        self.number_two = "com.google.android.dialer:id/two"
        self.number_three = "com.google.android.dialer:id/three"
        self.number_four = "com.google.android.dialer:id/four"
        self.number_five = "com.google.android.dialer:id/five"
        self.number_six = "com.google.android.dialer:id/six"
        self.number_seven = "com.google.android.dialer:id/seven"
        self.number_eight = "com.google.android.dialer:id/eight"
        self.number_nine = "com.google.android.dialer:id/nine"
        self.button_call = "com.google.android.dialer:id/dialpad_voice_call_button"
        self.end_call_button = "com.google.android.dialer:id/incall_end_call"
        self.displayed_number = "com.google.android.dialer:id/contactgrid_contact_name"
        self.full_num = ""

    def click_on_dial_pad(self):
        """Press the button in the phone to dial the phone number"""
        dial_pad_element = self.driver.find_element(by=AppiumBy.ID,value=self.dial_pad)
        dial_pad_element.click()

    def click_phone_number(self,num_to_click):
            """Clicking on the corresponding digit of the phone number"""
            if num_to_click == "0":
                element = self.driver.find_element(by=AppiumBy.ID, value=self.number_zero)
            elif num_to_click == "1":
                element = self.driver.find_element(by=AppiumBy.ID, value=self.number_one)
            elif num_to_click == "2":
                element = self.driver.find_element(by=AppiumBy.ID, value=self.number_two)
            elif num_to_click == "3":
                element = self.driver.find_element(by=AppiumBy.ID, value=self.number_three)
            elif num_to_click == "4" :
                element = self.driver.find_element(by=AppiumBy.ID, value=self.number_four)
            elif num_to_click == "5":
                element = self.driver.find_element(by=AppiumBy.ID, value=self.number_five)
            elif num_to_click == "6":
                element = self.driver.find_element(by=AppiumBy.ID, value=self.number_six)
            elif num_to_click == "7":
                element = self.driver.find_element(by=AppiumBy.ID, value=self.number_seven)
            elif num_to_click == "8":
                element = self.driver.find_element(by=AppiumBy.ID, value=self.number_eight)
            elif num_to_click == "9":
                element = self.driver.find_element(by=AppiumBy.ID, value=self.number_nine)
            element.click()

    def dial_num(self, full_num):
        """Dialing a full phone number"""
        self.full_num = full_num
        for num in full_num:
            self.click_phone_number(num)

    def click_on_call_button(self):
        """Click on the call button to make a call"""
        call = self.driver.find_element(by=AppiumBy.ID, value=self.button_call)
        call.click()

    def element_end_call_button(self):
        """Return element for end call button"""
        end_call = self.driver.find_element(by=AppiumBy.ID, value=self.end_call_button)
        return end_call

    def click_on_end_call_button(self):
        """Click on the end call button to end the call"""
        end_call = self.driver.find_element(by=AppiumBy.ID, value=self.end_call_button)
        end_call.click()

    def displayed_phone_number(self):
        """Return the displayed phone number when calling"""
        number = self.driver.find_element(by=AppiumBy.ID, value=self.displayed_number)
        displayed_number = number.text
        clean_string = re.sub(r'\D', '', displayed_number)
        return clean_string

    def send_message(self):
        """Sends a message if the phone starts at 05"""
        if self.full_num[:2] == "05":
            send = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@text='Send a message']")
            send.click()
        else:
            print(f"It's impossible to send an SMS to this number: {self.full_num} ")

    def valid_phone_number_for_message(self):
        """Returns valid or not valid phone number"""
        return self.full_num[:2] == "05"


