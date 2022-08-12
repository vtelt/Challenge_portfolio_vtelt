from pages.base_page import BasePage


class Dashboard(BasePage):
        scouts_panel_heading_xpath = "//*[@id='__next']/div[1]/header/div/h6"
        main_page_menu_item_xpath = "//div[contains(@class, 'jss397')]/ul[1]/div[1]/span"
        players_menu_item_xpath = "//div[contains(@class, 'jss397')]/ul[1]/div[2]/span"
        languange_menu_item_xpath = "//div[contains(@class, 'jss397')]/ul[2]/div[1]/span"
        sign_out_menu_item_xpath = "//div[contains(@class, 'jss397')]/ul[2]/div[2]/span"
        players_get_count_xpath = "//div[contains(@class, 'jss378')]/div[1]/div/div/following-sibling::div/b"
        matches_get_count_xpath = "//div[contains(@class, 'jss378')]/div[2]/div/div/following-sibling::div/b"
        reports_get_count_xpath = "//div[contains(@class, 'jss378')]/div[3]/div/div/following-sibling::div/b"
        events_get_count_xpath = "//div[contains(@class, 'jss378')]/div[4]/div/div/following-sibling::div/b"
        dev_team_contact_link_xpath = "//*[contains(@class, 'MuiCardActions-root')]/a"
        add_player_link_xpath = "//div[contains(@class, 'MuiGrid-root MuiGrid-container')]/div[2]/div/div/a"
        last_created_player_link_xpath = "//div[contains(@class, 'MuiGrid-root MuiGrid-container')]/div[3]/div/div/a[1]"
        last_updated_player_link_xpath = "//div[contains(@class, 'MuiGrid-root MuiGrid-container')]/div[3]/div/div/a[2]"
        last_updated_report_link_xpath = "//div[contains(@class, 'MuiGrid-root MuiGrid-container')]/div[3]/div/div/a[3]"

        pass