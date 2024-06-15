import os

import pytest
import requests

import config
from api.update_status import UpdateStatusAPI
import json
from common.yaml_util import YamlUtil

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
            status = case_data.get("status")
            test_data.append(status)
    # 返回处理之后测试数据
    return test_data

class TestUpdateStatusAPI:
    def setup_method(self):
        self.update_api = UpdateStatusAPI()

    @pytest.mark.parametrize("status",build_data(json_file=config.BASE_PATH + "\\data\\updateStatus.json"))
    def test01_update(self,status):
        token = YamlUtil().read_extract_yaml('token')
        headers = {
            'token': f'{token}'
        }
        res = self.update_api.updateStatus(status=status,headers=headers)
        print(res.json())
        # 使用code来做断言

    #测试未登录状态
    def test02_notLogin(self):
        res = requests.put(url=config.BASE_URL+'/admin/shop/1')
        assert res.json()['code']


















