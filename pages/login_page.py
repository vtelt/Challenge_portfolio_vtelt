from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    scouts_panel_heading_xpath = "//*[contains(@class, 'MuiTypography-root MuiTypography-h5')]"
    remind_password_hyperlink_xpath = "//a[contains(@class, 'MuiTypography-root')]"
    remind_password_header_xpath = "//h5[contains(@class, 'MuiTypography-root')]"
    email_field_xpath = "//*[@name='email']"
    back_to_sign_in_link_xpath = "//a[contains(@class, 'MuiTypography-root')]"
    language_dropdown_xpath = "//*[contains(@class, 'MuiSelect-root MuiSelect-select')]"
    dropdown_polish_language_xpath = "//li[@data-value='pl']"
    dropdown_english_language_xpath = "//li[@data-value='en']"
    sign_in_send_button_xpath = "//*[@type='submit']/span[1]"
    login_url = "https://scouts.futbolkolektyw.pl/en/"
    expected_page_title = "Scouts panel - sign in"
    expected_box_header = "Scouts Panel"
    incorrect_login_message_xpath = "//span[contains(@class, 'MuiTypography-root')]"
    expected_invalid_login_message = "Identifier or password invalid."
    expected_empty_password_message = "Please provide your password."
    expected_remind_page_header = "Remind password"

    def type_to_login(self, login):
        self.field_send_keys(self.login_field_xpath, login)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_send_button_xpath)


    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_page_title

    def title_of_header(self):
        self.assert_element_text(self.driver, self.scouts_panel_heading_xpath, self.expected_box_header)

    def do_login(self, login, password):
        self.type_to_login(login)
        self.type_in_password(password)
        self.click_on_the_sign_in_button()

    def incorrect_login_check_message(self):
        self.assert_element_text(self.driver, self.incorrect_login_message_xpath, self.expected_invalid_login_message)

    def empty_password_check_message(self):
        self.assert_element_text(self.driver, self.incorrect_login_message_xpath, self.expected_empty_password_message)

    def click_on_remind_password(self):
        self.click_on_the_element(self.remind_password_hyperlink_xpath)

    def check_remind_page_title(self):
        self.assert_element_text(self.driver, self.remind_password_header_xpath, self.expected_remind_page_header)

    def click_on_back_to_sign_in(self):
        self.click_on_the_element(self.back_to_sign_in_link_xpath)

    def type_to_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)
