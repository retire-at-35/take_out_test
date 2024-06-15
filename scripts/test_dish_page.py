#测试菜品分页查询接口
import json
import pytest
import config
from api.dish  import DishAPI
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

class TestDish:
    def setup_method(self):
        self.dish_api = DishAPI()

    @pytest.mark.parametrize("page,pageSize,name,categoryId,status,total", build_data(json_file=config.BASE_PATH + "\\data\\dishPage.json"))
    def test_dish_page(self,page,pageSize,name,categoryId,status,total):
        token = YamlUtil().read_extract_yaml('token')
        headers = {
            'token': f'{token}'
        }
        testData = {
            "page": page,
            "pageSize": pageSize,
            "name": name,
            "categoryId": categoryId,
            "status": status
        }
        response = self.dish_api.page_search(headers=headers,test_data=testData)
        assert response.json()['data']['total'] == total




