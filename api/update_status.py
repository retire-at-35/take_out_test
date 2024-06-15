# 登录：
import requests
import config


# 创建接口类
class UpdateStatusAPI:
    # 初始化
    def __init__(self):
        # 指定url基本信息
        self.url_update_status = config.BASE_URL + "/admin/shop"


    # 登录
    def updateStatus(self, status,headers):
        self.url_update_status = self.url_update_status+"/"+status
        return requests.put(url=self.url_update_status,headers=headers)

