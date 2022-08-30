import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    scouts_panel = "//h6[contains(text(),'Scouts Panel')]"
    main_page_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    players_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    polski_xpath = "//span[contains(text(),'Polski')]"
    events_count_xpath = "//*[contains(text(),'Events count')]"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    last_created_player_xpath = "//*[text()='test_name test_surname']"
    dev_team_contact = "//span[contains(text(),'Dev team contact')]"
    logo_xpath = "//*[@title='Logo Scouts Panel']"
    sign_out_block_xpath = "//*[text()='Sign out']"

    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    pass