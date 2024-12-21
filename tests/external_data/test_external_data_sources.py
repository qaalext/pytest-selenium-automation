import pytest
from pages.FacebookPage import FaceBookPage
from base.utilities.resultsstatus import ResultsStatus
from base.utilities.read_data_files import getCSVData
from ddt import ddt, data, unpack
import unittest

@pytest.mark.usefixtures("oneTimeSetUpv2")
@ddt
class ExternalDataSourcesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUpv2):
        self.fb = FaceBookPage(self.driver)
        self.ts = ResultsStatus(self.driver)

    @pytest.mark.external
    @data(*getCSVData("C:\\Users\\arend\OneDrive\Desktop\\automation_fw\external_data\login.csv"))
    @unpack
    def test_multiple_login_scenarios_on_fb(self, email, password):
        self.fb.go_to_fb()
        self.fb.fb_login(email, password)
        self.fb.sleep(5)
        result = self.fb.check_title_contains_facebook_keyword()
        self.ts.markFinal("login to fb with multiple acccount ", result, "could not login")

