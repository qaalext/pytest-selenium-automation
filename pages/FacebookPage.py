

from base.selenium_driver import SeleniumDriver
from base.utilities import custom_logger as cl
import logging

class FaceBookPage(SeleniumDriver):
    log = cl.customLogger(logging.INFO)

    # def __init__(self, driver):
    #
    #     super(LoginPage, self).__init__(driver)
    #     self.driver = driver

    _fb_url = "https://www.facebook.com/"
    _fb_email = "email"
    _fb_password = "pass"
    _fb_login_btn = "u_0_b"




    def go_to_fb(self):
        self.go_to_url(self._fb_url)

    def enter_email(self, email):
        self.sendKeys(email, self._fb_email, locatorType="id")

    def enter_pass(self, password):
        self.sendKeys(password, self._fb_password, locatorType="id")

    def click_login_bb_btn(self):
        self.elementClick(self._fb_login_btn, locatorType="id")

    def fb_login(self, email, password):
        self.enter_email(email)
        self.enter_pass(password)
        self.click_login_bb_btn()

    def check_password_field_to_match_expected_result(self, expected):
        if expected == self.isElementPresent(self._fb_password, locatorType="id"):
            return True
        return False

    def check_title_contains_facebook_keyword(self):
        return self.verifyTextContains(self.getTitle(), "Facebook")
