from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    scouts_panel_heading_xpath = "//*[contains(@class, 'MuiTypography-root MuiTypography-h5')]"
    remind_password_hyperlink_xpath = "//a[contains(@class, 'MuiTypography-root')]"
    language_dropdown_xpath = "//*[contains(@class, 'MuiSelect-root MuiSelect-select')]"
    dropdown_polish_language_xpath = "//li[@data-value='pl']"
    dropdown_english_language_xpath = "//li[@data-value='en']"
    sign_in_send_button_xpath = "//*[@type='submit']/span[1]"
    login_url = "https://scouts-test.futbolkolektyw.pl/"
    expected_page_title = "Scouts panel - sign in"
    expected_box_header = "Scouts Panel"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_send_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_page_title

    def title_of_header(self):
        self.assert_element_text(self.driver, self.scouts_panel_heading_xpath, self.expected_box_header)
