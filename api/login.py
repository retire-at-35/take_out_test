# 登录：
import requests
import config


# 创建接口类
class LoginAPI:
    # 初始化
    def __init__(self):
        # 指定url基本信息
        self.url_login = config.BASE_URL + "/admin/employee/login"


    # 登录
    def login(self, test_data):
        return requests.post(url=self.url_login, json=test_data)

