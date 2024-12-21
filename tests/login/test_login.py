import pytest
import unittest

from pages.LoginPage import LoginPage
from base.utilities.resultsstatus import ResultsStatus

@pytest.mark.usefixtures("oneTimeSetUpv2", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUpv2):
        self.ts = ResultsStatus(self.driver)
        self.lp = LoginPage(self.driver)



    @pytest.mark.login
    def test_login_spiru(self):
        self.lp.go_to_blackboard()
        self.lp.bb_login(LoginPage.email, LoginPage.password)
        result = self.lp.check_if_username_matches()
        self.ts.markFinal("Verificare username", result, "Username incorect")

