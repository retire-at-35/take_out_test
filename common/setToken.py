import requests
import config
from common.yaml_util import YamlUtil
login_data = {
            "username": 'admin',
            "password": '123456',
        }
res = requests.post(url=config.BASE_URL + "/admin/employee/login",json=login_data)
        # print(res.json())
token = res.json()['data']['token']
YamlUtil().write_extract_yaml({'token':token})













