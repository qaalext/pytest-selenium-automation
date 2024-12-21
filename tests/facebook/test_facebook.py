import pytest
from pages.FacebookPage import FaceBookPage
from base.utilities.resultsstatus import ResultsStatus
@pytest.mark.usefixtures("oneTimeSetUpv2")
class FaceBookTests(object):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUpv2):
        self.fb = FaceBookPage(self.driver)
        self.ts = ResultsStatus(self.driver)


    @pytest.mark.fb
    @pytest.mark.parametrize("username,  password, expected",
                             [
                             ("g3wtest01@gmail.com", "Tester123", False),
                             ("g3wtest01@gmail.com", "T", True),
                             ("T", "Tester123", True)
                              ]
                             )
    def test_multiple_login_scenarios_on_fb(self, username, password, expected):
        self.fb.go_to_fb()
        self.fb.fb_login(username, password)
        self.fb.sleep(5)
        result = self.fb.check_password_field_to_match_expected_result(expected)
        self.ts.markFinal("Scenarii multiple de login", result, "failed")


