import os
import time
import unittest

from selenium.webdriver.chrome.service import Service

from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_player_page import AddPlayer
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestDashboardPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en') #open the website
        self.driver.fullscreen_window() #open a browser in full size mode
        self.driver.implicitly_wait(IMPLICITLY_WAIT) #wait before you start testing
        self.name = "David"
        self.surname = "Beckham"
        self.full_name = self.name+" "+self.surname

    def test_add_player_on_dashboard(self):
        user_login = LoginPage(self.driver)
        user_login.do_login('user01@getnada.com', 'Test-1234') #login to the system
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_add_player() #click on add player link
        add_player = AddPlayer(self.driver)
        add_player.type_to_name(self.name) #enter name of the player
        add_player.type_to_surname(self.surname) #enter surname of the player
        add_player.select_age("12/12/1972") #enter age of the player
        add_player.select_leg("left") #select left leg of the player (you can change leg: all else value will be marked as right)
        add_player.type_to_main_position("captain") #select position of the player
        add_player.click_on_the_submit_button() #click on submit button
        add_player.verify_player_in_menu_to_be_appeared(self.full_name) #verify that name of the player appears in left menu
        time.sleep(3)




    @classmethod
    def tearDown(self):
        self.driver.quit() #close the browser after the test
