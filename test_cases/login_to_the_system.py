import os
import time
import unittest

from selenium.webdriver.chrome.service import Service

from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en') #open the website
        self.driver.fullscreen_window() #open a browser in full size mode
        self.driver.implicitly_wait(IMPLICITLY_WAIT) #wait before you start testing
        self.user_login = LoginPage(self.driver)
        self.dashboard_page = Dashboard(self.driver)

    def test_log_in_to_the_system(self):
        self.user_login.title_of_page() #check if the title of the opened page is correct
        self.user_login.title_of_header() #check that the item in the box above the login field is correct
        self.user_login.do_login('user01@getnada.com', 'Test-1234') #login to the system
        self.dashboard_page.title_of_page() #check if the title of the opened page is correct
        time.sleep(3)

    def test_incorrect_login_to_the_system(self):
        self.user_login.do_login('test', 'Test-1234') #login to the system with incorrect login
        self.user_login.incorrect_login_check_message() #check error message
        self.user_login.title_of_page() #check that user stays on the login page
        time.sleep(3)

    def test_empty_password(self):
        self.user_login.do_login('user01@getnada.com', '') #login to the system with empty password
        self.user_login.empty_password_check_message() #check error message
        self.user_login.title_of_page() #check that user stays on the login page
        time.sleep(3)

    def test_log_out(self):
        self.user_login.do_login('user01@getnada.com', 'Test-1234') #login to the system
        self.dashboard_page.wait_for_sign_out_will_be_visible() #wait for the menu item to be visible
        self.dashboard_page.click_on_sign_out_button() #log out
        self.user_login.title_of_page() #check that user is on the login page
        time.sleep(3)

    def test_remind_password(self):
        self.user_login.click_on_remind_password() #click on remind password
        self.user_login.check_remind_page_title() #check that user is on remind password page
        self.user_login.type_to_email('user01@getnada.com') #enter email
        self.user_login.click_on_the_sign_in_button() #click on send button
        self.user_login.click_on_back_to_sign_in() #click on back to sign in
        self.user_login.title_of_page()  # check that user is on the login pages
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit() #close the browser after the test
