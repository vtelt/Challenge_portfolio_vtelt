from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    scouts_panel_heading_xpath = "//*[contains(@class, 'MuiTypography-root MuiTypography-h5')]"
    remind_password_hyperlink_xpath = "//a[contains(@class, 'MuiTypography-root')]"
    language_dropdown_xpath = "//*[contains(@class, 'MuiSelect-root MuiSelect-select')]"
    dropdown_polish_language_xpath = "//li[@data-value='pl']"
    dropdown_english_language_xpath = "//li[@data-value='en']"
    sign_in_send_button_xpath = "//*[contains(@class, 'MuiTouchRipple-root')]"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
