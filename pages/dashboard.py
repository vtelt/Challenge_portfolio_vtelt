import time

from pages.base_page import BasePage


class Dashboard(BasePage):
        scouts_panel_heading_xpath = "(//div[contains(@class, 'MuiToolbar-root')])/h6"
        main_page_menu_item_xpath = "(//ul[contains(@class, 'MuiList-root')])[1]/div[1]/div/span"
        players_menu_item_xpath = "(//ul[contains(@class, 'MuiList-root')])[1]/div[2]/div/span"
        languange_menu_item_xpath = "(//ul[contains(@class, 'MuiList-root')])[2]/div[1]/div/span"
        sign_out_menu_item_xpath = "(//ul[contains(@class, 'MuiList-root')])[2]/div[2]/div/span"
        players_get_count_xpath = "(//div[contains(@class, 'MuiPaper-root')])[2]/div/b"
        matches_get_count_xpath = "(//div[contains(@class, 'MuiPaper-root')])[3]/div/b"
        reports_get_count_xpath = "(//div[contains(@class, 'MuiPaper-root')])[4]/div/b"
        events_get_count_xpath = "(//div[contains(@class, 'MuiPaper-root')])[5]/div/b"
        dev_team_contact_link_xpath = "//*[contains(@class, 'MuiCardActions-root')]/a"
        add_player_link_xpath = "(//div[contains(@class, 'MuiPaper-root')])[7]/div/a"
        last_created_player_link_xpath = "(//div[contains(@class, 'MuiPaper-root')])[8]/div/a[1]"
        last_updated_player_link_xpath = "(//div[contains(@class, 'MuiPaper-root')])[8]/div/a[2]"
        last_updated_report_link_xpath = "(//div[contains(@class, 'MuiPaper-root')])[8]/div/a[3]"

        expected_title = "Scouts panel"
        dashboard_url = "https://scouts-test.futbolkolektyw.pl/"

        def title_of_page(self):
            time.sleep(4)
            assert self.get_page_title(self.dashboard_url) == self.expected_title

