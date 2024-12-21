import time
import os
from base.utilities import custom_logger as cl


class FrameworkConfig:

    currentDirectory = os.path.dirname(__file__)

    # setup drivers paths
    chrome_driver_path = ".\drivers\chromedriver.exe"
    firefox_driver_path = ".\drivers\geckodriver.exe"

    # setup the testing environment
    environment_test_setup = "uat"
    # total time of waiting for an element availability
    total_time = 20
    # check interval to see if the element is available yet
    pause_interval_time = 2

    #sets the path to the screenshots folder
    screenshots_path = os.path.join(currentDirectory,".\\screenshots\\")

    # generates a html report if set to True
    generate_html_report = True

    generate_html_report_path = ".\\reports\\"

    def htnl_make_report(self):
        if self.generate_html_report is True:
            _report_time_stamp = time.strftime("Date %y-%m-%d Time %H-%M-%S", time.gmtime())

            # user path to the reports directory where the report will be generated
            html_folder_report_location = os.path.join(self.currentDirectory, self.generate_html_report_path)

            # DO NOT Modify this
            html_folder_path = html_folder_report_location + "Test_Run {}.html".format(_report_time_stamp)
            try:
                if not os.path.exists(html_folder_report_location):
                    os.makedirs(html_folder_report_location)
                return html_folder_path
            except:
                print("Exception occurred attempting to create the folder")
        else:
            cl.customLogger().info("Report generation is disabled from the environment config class")
