import requests
from api.loginApi import MtxLogin

class TestLogin:
    def setup_class(self):
        self.session = requests.Session()

        self.login_obj = MtxLogin()

    def test_login_success(self):
        data = {}