from selenium import webdriver
from config import FrameworkConfig


class WebDriver:

    def __init__(self, browser):

        self.browser = browser

    def getWebDriverInstance(self):
        if self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=FrameworkConfig.firefox_driver_path)
            driver.maximize_window()
            return driver
        elif self.browser == "chrome":
            driver = webdriver.Chrome(FrameworkConfig.chrome_driver_path)
            driver.maximize_window()
            return driver
        elif self.browser == "headless":
            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-gpu')
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--start-maximized")
            options.add_argument("--headless")

        else:
            driver = webdriver.Chrome(executable_path="C:\\Users\\arend\OneDrive\\Desktop\\automation_fw\\drivers\\chromedriver.exe")
            driver.maximize_window()
            return driver

