

from base.selenium_driver import SeleniumDriver
from base.utilities import custom_logger as cl
import logging

class GooglePage(SeleniumDriver):
    log = cl.customLogger(logging.INFO)

    # def __init__(self, driver):
    #
    #     super(GooglePage, self).__init__(driver)
    #     self.driver = driver


    _url = "https://www.google.ro/"

    _search_field = "q"
    _submit_btn = "btnK"
    _first_result_from_google_search_page = "//div[@id='rso']/div[1]/div/div[@class='rc']//a[@href='https://misn-b.spiruharet.ro/informatica']/h3[.='Informatică - Universitatea Spiru Haret']"


    def go_to_google(self):
        self.go_to_url(self._url)


    def enter_text_in_search_field(self, data):
        self.sendKeys(data, self._search_field, locatorType="name")

    def click_on_google_search_button(self):
        self.elementClick(self._submit_btn, locatorType="name")

    def check_if_first_result_matches(self):
        expected_result = "Drept - Universitatea Spiru Haret".lower()
        current_result = self.getText(self._first_result_from_google_search_page, locatorType="xpath").lower()
        if  current_result == expected_result:
            return True
        self.log.error(f"Current result '{current_result}' does not match with the expected result '{expected_result}' ")
        return False
