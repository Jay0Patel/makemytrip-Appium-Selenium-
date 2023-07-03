import pytest

from pages.launch_page import LaunchPage
from testcases import conftest


@pytest.mark.usefixtures("setup")
class TestingSkype():
    def test_case1(self):
        lp = LaunchPage(self.driver)
        lp.language_selection()
        lp.sign_up("json7753@gmail.com")
        lp.gmail_OTP()
        lp.OTP()