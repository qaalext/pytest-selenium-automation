

from base.selenium_driver import SeleniumDriver
from base.utilities import custom_logger as cl
import logging

class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.INFO)

    # def __init__(self, driver):
    #
    #     super(LoginPage, self).__init__(driver)
    #     self.driver = driver


    _bb_url = "https://ush.blackboard.com/"



    _bb_email = "user_id"
    _bb_password = "password"
    _bb_login_btn = "entry-login"

    _cookie_accept_btn = "agree_button"
    _username = "a#global-nav-link"

    email = "1901025440010"
    password = "MAGDALENA"

    def go_to_blackboard(self):
        self.go_to_url(self._bb_url)


    def enter_email(self, email):
        self.sendKeys(email, self._bb_email, locatorType="id")

    def enter_pass(self, password):
        self.sendKeys(password, self._bb_password, locatorType="id")

    def click_login_bb_btn(self):
        self.elementClick(self._bb_login_btn)

    def get_username(self):
        return self.getText(self._username, locatorType="css").lower()

    def bb_login(self, email, password):
        self.elementClick(self._cookie_accept_btn)
        self.enter_email(email)
        self.enter_pass(password)
        self.click_login_bb_btn()

    def check_if_username_matches(self):
        actual = self.get_username()
        print(actual)
        expected =  "ALEXANDRU - TIBERIU RENDEC".lower()
        print(expected)
        return  self.verifyTextContains(actual, expected)
