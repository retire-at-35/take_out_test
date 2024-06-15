# 测试统计接口
# 这里只测试用户和营业额
import json

import pytest

import config
from api.statistic  import StatisticAPI
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
            begin = case_data.get("begin")
            end = case_data.get("end")
            code = case_data.get("code")
            test_data.append((begin,end,code))
    # 返回处理之后测试数据
    return test_data

class TestStatistic:
    def setup_method(self):
        self.statistic_api = StatisticAPI()

    #测试获取营业额
    @pytest.mark.parametrize("begin, end, code", build_data(json_file=config.BASE_PATH + "\\data\\statistic.json"))
    def test01_get_turnover(self,begin,end,code):
        token = YamlUtil().read_extract_yaml('token')
        data = {
            "begin": begin,
            "end": end,
            "code": code
        }
        headers = {
            'token': f'{token}'
        }
        res = self.statistic_api.turnoverStatistic(test_data=data,headers=headers)
        assert code == res.json()[code]

    #测试导出文件
    def test02_export_excel(self):
        token = YamlUtil().read_extract_yaml('token')
        headers = {
            'token': f'{token}'
        }
        response = self.statistic_api.exportExcel(headers=headers)
        # 检查响应的状态码是否为200
        assert response.status_code == 200, "导出文件接口请求失败"


