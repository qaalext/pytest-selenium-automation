# -*- coding: utf-8 -*-

import logging
import os
import time
import traceback
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, \
    ElementNotSelectableException, StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from base.utilities import custom_logger as cl
from config import FrameworkConfig
"""

Please note that the methods from this class will be used to create PAGE Objects 

DO NOT REMOVE unittest.TestCase FROM THE TEST CLASSES

"""
from selenium.webdriver.support.ui import WebDriverWait



class SeleniumDriver:
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.config = FrameworkConfig()

    def go_to_url(self, url):
        return self.driver.get(url)



    def screenShot(self, resultMessage):
        fileName = resultMessage  + " " + str(time.strftime("%d-%m-%H-%M-%S", time.gmtime())) + ".png"
        screenshotDirectory = self.config.screenshots_path
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory,
                                       relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)
        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory: " + destinationFile)
        except Exception as e:
            self.log.error("### screenShot exception occurred !", e)

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT

        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElementList(self, locator, locatorType="id"):
        # element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except NoSuchElementException as e:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
            raise e
        return element

    def getElement(self, locator, locatorType, timeout_seconds=FrameworkConfig.total_time):
        element = None
        pause_interval = FrameworkConfig.pause_interval_time
        retries = timeout_seconds
        while retries > 0:
            try:
                locatorType = locatorType.lower()
                byType = self.getByType(locatorType)
                element = self.driver.find_element(byType, locator)
                break
            except NoSuchElementException as e:
                if retries <= pause_interval:
                    self.log.info(f"Element '{locator}' could not be found despite waiting for {timeout_seconds} seconds, exception : {e}", exc_info=True)
                    raise  e
                else:
                    pass
            retries = retries - pause_interval
            self.log.info(f"Waiting for the element '{locator}' {pause_interval} more seconds to be displayed ")
            time.sleep(pause_interval)
        return element


    def elementClick(self, locator="", locatorType="id", timeout_seconds=FrameworkConfig.total_time):
        pause_interval = FrameworkConfig.pause_interval_time
        retries = timeout_seconds
        while retries > 0:
            try:
                locatorType = locatorType.lower()
                byType = self.getByType(locatorType)
                element = self.driver.find_element(byType, locator)
                if EC.element_to_be_clickable(element) and element.is_displayed():
                    return element.click()
            except Exception as e:
                if retries <= pause_interval:
                    self.log.info(f"Could not click on the element '{locator}' despite waiting for {timeout_seconds} seconds, exception : {e}", exc_info=True)
                    raise  e
                else:
                    pass
            retries = retries - pause_interval
            self.log.info(f"Waiting for the element '{locator}' {pause_interval} more seconds to be clickable ")
            time.sleep(pause_interval)



    def sendKeys(self, data, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
        except NoSuchElementException as e:
            self.log.error(f"Cannot send data on the element '{element}', with  locatorType '{locatorType}' {e}")
            raise Exception(f"Cannot send data on the element '{element}', with  locatorType '{locatorType}' {e}")


    def jsClick(self, locator="", locatorType="id"):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
                self.driver.execute_script("arguments[0].click();", element)

        except Exception as e:
            self.log.info("JS Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            raise  e


    def checkIfDisplayed(self, locator, locatorType):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
                if element.is_displayed():
                    return True
            self.log.info(f"Element : '{locator}' with locator type  '{locatorType}' not visible ")
            return False

        except ElementNotVisibleException as e:
            self.log.info("Element not visible : " + locator +
                          " locatorType: " + locatorType)
            raise  e



    def compare_urls(self, expected_url, timeout_seconds=FrameworkConfig.total_time):
        getUrl = None
        pause_interval = FrameworkConfig.pause_interval_time
        retries = timeout_seconds
        while retries > 0:
            try:
                getUrl = self.driver.current_url
                getUrl = getUrl.lower()
                expected_url = expected_url.lower()
                if getUrl == expected_url:
                                self.log.info(f"'{expected_url}' matches with the actual url {getUrl}")
                                return True and getUrl
            except Exception as e:
                if retries <= pause_interval:
                    self.log.info(f"exception : {e}", exc_info=True)
                    raise  e
                else:
                    pass
            retries = retries - pause_interval
            self.log.info(f"Waiting for the url '{getUrl}' {pause_interval} to be as expected {expected_url}")
            time.sleep(pause_interval)
        self.log.info(f"Actual Url '{getUrl}' does not match the expected one '{expected_url}'")
        return False

    def switch_to_frame(self, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.driver.switch_to.frame(element)
                self.log.info("Switched to iframe" + " " + str(locator))

        except Exception as e:
            self.log.error("Could not switch to iframe" + " " + str(locator))
            raise e

    def switch_to_default_frame(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            self.log.error(f"Could not switch to default after iframe {e}")
            raise e

    def select_window(self, number_of_window):
        try:
            window_after = self.driver.window_handles[number_of_window]
            self.driver.switch_to.window(window_after)

        except Exception as e:
            self.log.info(f"Could not find the window to select {e}")
            raise e

    def close_popup_window(self):
        try:
            current_handle = self.driver.current_window_handle
            default_handle = self.driver.window_handles[0]
            handles = list(self.driver.window_handles)
            if default_handle != current_handle:
                handles.remove(current_handle)
                self.driver.switch_to_window(default_handle)

        except Exception as e:
            self.log.info("could not switch to default handle", {e})
            raise e


    def getTitle(self, timeout_seconds=FrameworkConfig.total_time):
        pause_interval = FrameworkConfig.pause_interval_time
        retries = timeout_seconds
        while retries > 0:
            try:
                self.log.info(f"{self.driver.title}")
                return self.driver.title
            except Exception as e:
                if retries <= pause_interval:
                    self.log.info(f"Could not get the title : {e}", exc_info=True)
                    raise  e
                else:
                    pass
            retries = retries - pause_interval
            time.sleep(pause_interval)


    def get_current_url(self, timeout_seconds=FrameworkConfig.total_time):
        pause_interval = FrameworkConfig.pause_interval_time
        retries = timeout_seconds
        while retries > 0:
            try:
                self.log.info(f"{self.driver.current_url}")
                return self.driver.current_url
            except Exception as e:
                if retries <= pause_interval:
                    self.log.info(f"Could not get the page url : {e}", exc_info=True)
                    raise e
                else:
                    pass
            retries = retries - pause_interval
            time.sleep(pause_interval)



    def check_if_element_enabled(self, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            if element.is_enabled():
                self.log.info("Element is enabled ")
                return element
            return self.log.error("Element is not enabled") and element
        except Exception as e:
            self.log.error(f"Element is not enabled {e}")
            raise e



    def open_url_in_another_tab(self, url):
        self.driver.execute_script('''window.open("about:blank");''')
        self.select_window(1)
        self.driver.get(url)


    def sendKeysAndPressEnter(self, data, locator="", locatorType="id",
                              element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data, Keys.ENTER)

        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                          " locatorType: " + locatorType)


    def getText(self, locator="", locatorType="id", element=None,
                info=""):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info(f"The text is :: '{text}'")
                text = text.strip()
        except Exception as e:
            self.log.error(f"Failed to get text on element {e} ")
            raise e
        return text

    def get_text_attribute(self, locator="", locatorType="id", attributeType="", element=None,
                           info="", ):

        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            text = element.get_attribute(attributeType)
            self.log.info("The text is :: '" + text + "'")
            text = text.strip()
        except Exception as e:
            self.log.error(f"Failed to get text on element  {e}" )
            raise e
        return text

    def isElementPresent(self, locator="", locatorType="id",
                         element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except Exception as e:
            self.log.error(f"Element not found  {e}")
            return False



    def webScroll(self, direction="up", value=""):
        """
        used to scroll down or up the webpage
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -{});".format(value))

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, {});".format(value))

    def go_back(self):
        try:

            self.driver.execute_script("window.history.go(-1)")
        except Exception as e:
            self.log.error("Exception occurred when executing go_back")
            raise e

    def clear_input_fields(self, locator="", locatorType=""):
        try:
            field = self.getElement(locator, locatorType)
            field.clear()
        except Exception as e:
            self.log.error(f"Could not clear the input fields {e}")
            raise e


    def sleep(self, sec, info=""):
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()


    def verifyTextContains(self, actualText, expectedText):

        if expectedText.lower() in actualText.lower():

            return True
        else:
            self.log.info("### Not found")
            return False

    def check_page_title(self, titleToVerify):
        try:
            actualTitle = self.getTitle()
            return self.verifyTextContains(actualTitle, titleToVerify)
        except Exception as e:
            self.log.error(f"Failed to get page title {e}")
            return False


