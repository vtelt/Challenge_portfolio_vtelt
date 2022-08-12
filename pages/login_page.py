from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_send_button_xpath = "//*[contains(@class, 'MuiTouchRipple-root')]"
    scouts_panel_heading_xpath = "//*[text()='Scouts Panel']"
    remind_password_hyperlink_xpath = "//a[contains(text(), 'Remind password')]"
    language_dropdown_xpath = "//*[contains(@class, 'MuiSelect-root MuiSelect-select')]"
    dropdown_polish_language_xpath = "//li[@data-value='pl']"
    dropdown_english_language_xpath = "//li[@data-value='en']"
    #Remind password form elements:
    remind_password_heading_xpath = "//*[contains(@class, 'MuiTypography-root MuiTypography-h5')]"
    email_input_xpath = "//*[@name='email']"
    back_to_sign_in_xpath = "//*[text()='Back to sign in']"
    #send button with the same xpath as sign_in button
    #language dropdown is the same as previous

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
