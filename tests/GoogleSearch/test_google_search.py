import pytest
import unittest

from pages.GooglePage import GooglePage
from base.utilities.resultsstatus import ResultsStatus

@pytest.mark.usefixtures("oneTimeSetUpv2", "setUp")
class GoogleSearchTests(unittest.TestCase):
    always_false_for_skip_example = False
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUpv2):
        self.ts = ResultsStatus(self.driver)
        self.gp = GooglePage(self.driver)



    @pytest.mark.spiru
    def test_if_first_result_matches_spiru_haret_university(self):
        if not self.always_false_for_skip_example:
            pytest.skip("Acesta este un exemplu de skip")
        self.gp.go_to_google()
        self.gp.enter_text_in_search_field("spiru haret informatica")
        self.gp.click_on_google_search_button()
        result = self.gp.check_if_first_result_matches()
        self.ts.markFinal("Check if spiru in first result", result, "Spiru not in first result")















    # def test_access_google(self):
    #     self.lp.go_to_google()
    #     # self.lp.getElement("Q", locatorType="name")
    #     self.lp.sendKeys("A", "q", locatorType="name")
    #     result =  False
    #     self.lp.sleep(2)
    #
    #     self.ts.markFinal("invalid GoogleSearch check", result, "GoogleSearch success")


    # def test_report(self):
    #     self.lp.go_to_google()
    #     # self.lp.getElement("Q", locatorType="name")
    #     # self.lp.sendKeys("A", "q", locatorType="name")
    #     result =  False
    #     self.ts.markFinal("invalid GoogleSearch check", result, "GoogleSearch success")
    #     # self.lp.sleep(2)
    #     # assert False



    # def test_access_check_if_displayed(self):
    #     self.lp.go_to_google()
    #     result = self.lp.checkIfDisplayed("q", locatorType="name")
    #     self.ts.markFinal("display test", result, "is not displayed")

    # def test_check_if_url_is_as_expected(self):
    #     self.lp.go_to_google()
    #     result = self.lp.compare_urls("https://www.Google.Com/")
    #     self.ts.markFinal("display test", result, "is not displayed")

    # def test_get_title_get_url(self):
    #     self.lp.go_to_google()
    #     self.lp.getTitle()
    #     self.lp.get_current_url()


    # def test_super_in_pyth(self):
    #     self.gp.go_to_url(self._club_url)
    #     self.gp.login_on_club("g3w-test01@test.com", "Tester123")
    #     self.gp.sleep(10)


    # def test_access_google_and_click_search(self):
    #     self.lp.go_to_google()
    #     # self.lp.getElement("Q", locatorType="name")
    #     start = datetime.datetime.now().second
    #     self.lp.sendKeys("A", "q", locatorType="name")
    #     self.lp.elementClick("abtnK", locatorType="name")
    #     end = datetime.datetime.now().second - start
    #     print(end)
    #     self.lp.sleep(15)

    # def test_element_is_never_found(self):
    #     self.lp.go_to_google()
    #     self.lp.getElement("q", locatorType="name")
    #     self.lp.sleep(5)




    # def test_connv3(self):
    #     url = "https://connect.ubisoft.com/create?appId=412802ed-8163-4642-a931-8299f209fecb&nexturl=https:%2F%2Foverlay.ubisoft.com%2Foverlay-connect-integration%2Fdemo.html&genomeId=&lang=en-US"
    #     self.lp.go_to_url(url)
    #     _accept_terms_css = "input#tosCheckbox"
    #     self.lp.click_on_hidden_elements(_accept_terms_css, locatorType="id")
    #     # self.lp.sleep(5)









    # def getElement(self, locator, locatorType, timeout_seconds=FrameworkConfig.total_time):
    #     pause_interval = FrameworkConfig.pause_interval_time
    #     retries = timeout_seconds
    #     while retries:
    #         try:
    #             locatorType = locatorType.lower()
    #             byType = self.getByType(locatorType)
    #             element = self.driver.find_element(byType, locator)
    #             if  EC.element_to_be_clickable(element) and element.is_displayed():
    #                 return element
    #         except NoSuchElementException as e:
    #             if retries <= 2:
    #                 # self.log.info(f"Element '{locator}' could not be found despite waiting for {timeout_seconds} seconds, exception : {e}", exc_info=True)
    #                 raise  e
    #             else:
    #                 pass
    #         retries = retries - pause_interval
    #         self.log.info(f"Waiting for the element '{locator}' {timeout_seconds} more seconds to be displayed ")
    #         time.sleep(pause_interval)
    #
    #
    #
    #
    #
    #
    # def sendKeys(self, data, locator="", locatorType="id", element=None):
    #
    #     try:
    #         if locator:
    #             element = self.getElement(locator, locatorType)
    #         element.send_keys(data)
    #     except NoSuchElementException as e:
    #         raise Exception(f"Cannot send data on the element '{element}', with  locatorType '{locatorType}' {e}")
