"""
@package utilities


It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
from base.utilities import custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver
# this is used for the assert function in test cases


class ResultsStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO) # helps writing info / logs in the automation log file about tests being marked as PASSED / FAILED

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(ResultsStatus, self).__init__(driver)
        self.resultList = []  #list with the results Passed / Failed

    def setResult(self, result, resultMessage):
        try:
            if result is not None:  # first checks if the result is None in order to further check for True and False
                if result:
                    self.resultList.append("PASS") # marks the results as Passed when the result is True
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else:
                    self.resultList.append("FAIL") #marks the tests as failed when the result is FaLSE
                    self.log.info("### VERIFICATION FAILED :: + " + resultMessage)
                    self.screenShot(resultMessage) # is inherited from screenshot method to take automatically screenshots of failure without calling the method
            else:
                self.resultList.append("FAIL")  #marks the tests as failed when the reuslt is None
                self.log.error("### VERIFICATION FAILED [result None] :: + " + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL") #marks the tests as failed when the an exception occurs
            self.log.error("### Exception Occurred !!!")
            self.screenShot(resultMessage)


    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result, resultMessage)
        if "FAIL" in  self.resultList:
            self.log.error(testName + " ### TEST FAILED")
            self.resultList.clear()
            assert False
        else:
            self.log.info(testName + "### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True


        # this methods checks all the verification points from the mark method
        # and if any of the verification points from the mark method are failed
        # it will fail the entire test
        # else it will mark the result as true
        # Note that this method is setting the test as Failed or Passed
