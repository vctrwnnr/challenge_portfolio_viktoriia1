import os
import time
import unittest

from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestDashboardPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.name = "James"
        self.surname = "Bond"

    def test_add_player_to_dash_board(self):
        user_login = LoginPage(self.driver)
        user_login.type_all_for_log_in('user01@getnada.com', 'Test-1234')
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_add_player_button()
        add_player = AddPlayer(self.driver)
        add_player.type_player_name(self.name)
        add_player.type_player_surname(self.surname)
        add_player.select_player_age("11/11/1920")
        add_player.choose_leg("left")
        add_player.type_to_main_position("captain")
        add_player.click_submit_button()
        time.sleep(5)
        add_player.click_main_page_button()
        time.sleep(4)

    @classmethod
    def tearDown(self):
        self.driver.quit()