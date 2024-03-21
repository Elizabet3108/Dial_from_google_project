from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver as selenium_webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
from appium import webdriver as appium_webdriver
from globals import (appium_server_url_local, capabilities, google_website, text_for_test1, message_for_test1,
                     text_for_test2, message_for_test2, text_for_test3, text_for_test4)
from pages.Main_google_page import Main_google_page
from pages.Search_results_google_page import Search_results_page
from pages.Dial_phone_page import Dial_phone_page
from pages.Send_message_page import Send_message_page

class Test_Appium_Selenium(unittest.TestCase):
    def setUp(self):
        capabilities["appPackage"] = "com.google.android.dialer"
        capabilities["appActivity"] = ".extensions.GoogleDialtactsActivity"
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver_selenium = selenium_webdriver.Chrome(service=service)
        self.driver_selenium.get(google_website)
        self.driver_appium = appium_webdriver.Remote(appium_server_url_local, capabilities)
        self.driver_appium.implicitly_wait(10)
        self.dial_phone_page = Dial_phone_page(self.driver_appium)
        self.main_google_page = Main_google_page(self.driver_selenium)

    # 1. Open Google Chrome by selenium
    # 2. Search text: Jetsurf Israel
    # 3. Get phone number from results
    # 4. Open tested phone device by appium
    # 5. Dial a phone number by appium
    # 6. Send message to phone number

    def test1_send_message_with_valid_phone_number(self):
        """The test checks that if the phone number start with '05', then message will be sent"""
        send_message_page = Send_message_page(self.driver_appium)
        self.main_google_page.search_text(text_for_test1)
        results_page = Search_results_page(self.driver_selenium)
        dial_phone_number = results_page.get_phone_number()
        self.dial_phone_page.click_on_dial_pad()
        self.dial_phone_page.dial_num(dial_phone_number)
        if self.dial_phone_page.valid_phone_number_for_message():
            self.dial_phone_page.send_message()
            send_message_page.send_text_to_message(message_for_test1)
            send_message_page.click_on_send()
        else:
            self.dial_phone_page.send_message()

        self.assertEqual(dial_phone_number, send_message_page.displayed_phone_number(),
                         "The number that was dialed and the number to whom the message was sent match")
        self.assertEqual("I have some questions about the surf boards", send_message_page.sent_message())

        send_message_page.click_on_option()
        send_message_page.click_on_delete()
        send_message_page.confirmation_of_deletion()

        # 1. Open Google Chrome by selenium
        # 2. Search text: galim surf school
        # 3. Get phone number from results
        # 4. Open tested phone device by appium
        # 5. Dial a phone number by appium
        # 6. Send message to phone number

    def test2_send_message_with_invalid_phone_number(self):
        """The test checks that if the number doesn't start with '05', then can't send a message"""
        send_message_page = Send_message_page(self.driver_appium)
        self.main_google_page.search_text(text_for_test2)
        results_page = Search_results_page(self.driver_selenium)
        dial_phone_number = results_page.get_phone_number()
        self.dial_phone_page.click_on_dial_pad()
        self.dial_phone_page.dial_num(dial_phone_number)
        if self.dial_phone_page.valid_phone_number_for_message():
            self.dial_phone_page.send_message()
            send_message_page.send_text_to_message(message_for_test2)
            send_message_page.click_on_send()
        else:
            self.dial_phone_page.send_message()

        self.assertNotEqual(dial_phone_number[:2], "05", "The phone number doesn't start with '05'")

        # 1. Open Google Chrome by selenium
        # 2. Search text: galim surf school
        # 3. Get phone number from results
        # 4. Open tested phone device by appium
        # 5. Dial a phone number by appium
        # 6. Reset the call

    def test3_galim(self):
        """The test checks if the phone number from the site matches its dial and that there ia a button on the phone to
        end the call"""
        self.main_google_page.search_text(text_for_test3)
        results_page = Search_results_page(self.driver_selenium)
        dial_phone_number = results_page.get_phone_number()
        self.dial_phone_page.click_on_dial_pad()
        self.dial_phone_page.dial_num(dial_phone_number)
        self.dial_phone_page.click_on_call_button()
        time.sleep(3)
        displayed_number = self.dial_phone_page.displayed_phone_number()

        self.assertIsNotNone(self.dial_phone_page.element_end_call_button(), "Element not found")
        self.dial_phone_page.click_on_end_call_button()

        self.assertEqual(dial_phone_number, displayed_number)

    # 1. Open Google Chrome by selenium
    # 2. Search text: country beit barbur tel aviv
    # 3. Get phone number from results
    # 4. Open tested phone device by appium
    # 5. Dial a phone number by appium
    # 6. Reset the call

    def test4_community_country(self):
        """The test checks if the phone number from the site matches its dial and that there ia a button on the phone to
        end the call"""
        self.main_google_page.search_text(text_for_test4)
        results_page = Search_results_page(self.driver_selenium)
        dial_phone_number = results_page.get_phone_number()
        self.dial_phone_page.click_on_dial_pad()
        self.dial_phone_page.dial_num(dial_phone_number)
        self.dial_phone_page.click_on_call_button()
        time.sleep(3)
        displayed_number = self.dial_phone_page.displayed_phone_number()

        self.assertIsNotNone(self.dial_phone_page.element_end_call_button(), "Element not found")
        self.dial_phone_page.click_on_end_call_button()

        self.assertEqual(dial_phone_number, displayed_number)

    def tearDown(self):
        self.driver_selenium.quit()
        self.driver_appium.quit()





