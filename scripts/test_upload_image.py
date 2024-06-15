import pytest
import requests

import config
from common.yaml_util import YamlUtil


# 上传成功
def test01_upload_success():
    token = YamlUtil().read_extract_yaml('token')
    headers = {
        'token': f'{token}'
    }
    f = open(config.BASE_PATH + "/data/test.jpg", "rb")
    response = requests.post(url=config.BASE_URL+'/admin/common/upload',files={"file": f},headers=headers)
    assert response.status_code == 200


# 文件类型不对
def test02_upload_failure():
    token = YamlUtil().read_extract_yaml('token')
    headers = {
        'token': f'{token}'
    }
    f = open(config.BASE_PATH + "/data/git.doc", "rb")
    response = requests.post(url=config.BASE_URL+'/admin/common/upload',files={"file": f},headers=headers)
    assert response.status_code == 200

# 图片大小过大
def test03_upload_failure():
    token = YamlUtil().read_extract_yaml('token')
    headers = {
        'token': f'{token}'
    }
    f = open(config.BASE_PATH + "/data/big.jpg", "rb")
    response = requests.post(url=config.BASE_URL+'/admin/common/upload',files={"file": f},headers=headers)
    assert response.status_code == 200

# 图片数据为空
def test03_upload_failure():
    token = YamlUtil().read_extract_yaml('token')
    headers = {
        'token': f'{token}'
    }
    response = requests.post(url=config.BASE_URL+'/admin/common/upload',files={"file": None},headers=headers)
    assert response.status_code == 200