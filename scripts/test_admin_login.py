import os

import pytest

import config
from api.login import LoginAPI
import json


def build_data(json_file):
    # 定义空列表
    test_data = []
    # 打开json文件
    with open(json_file, "r") as f:
        # 加载json文件数据
        json_data = json.load(f)
        # 循环遍历测试数据
        for case_data in json_data:
            # 转换数据格式[{},{}] ==> [(),()]
            username = case_data.get("username")
            password = case_data.get("password")
            code = case_data.get("code")
            test_data.append((username, password, code))
    # 返回处理之后测试数据
    return test_data

class TestLoginAPI:
    def setup_method(self):
        self.login_api = LoginAPI()

    @pytest.mark.parametrize("username, password, code",build_data(json_file=config.BASE_PATH + "\\data\\login.json"))
    def test01_success(self,username,password,code):
        login_data = {
            "username": username,
            "password": password,
        }
        res = self.login_api.login(test_data=login_data)
        # print(res.json())
        print(res.json()['data']['token'])
        # 使用code来做断言
        assert res.json()['code'] == code

















