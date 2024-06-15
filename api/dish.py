import requests
import config


# 创建接口类
class DishAPI:
    # 初始化
    def __init__(self):
        # 指定url基本信息
        self.url_page_search = config.BASE_URL + "/admin/dish/page"
        self.url_save = config.BASE_URL + "/admin/dish"
        self.url_update = config.BASE_URL + "/admin/dish/"
        self.url_update_status = config.BASE_URL + "/admin/dish/status"


    # 分页查询
    def page_search(self, test_data,headers):
        return requests.get(url=self.url_page_search, json=test_data,headers=headers)

    # 菜品新增
    def dish_save(self,test_data,headers):
        return requests.post(url=self.url_save,json=test_data,headers=headers)

    # 菜品修改
    def dish_update(self,test_data,headers):
        return requests.put(url=self.url_update,json=test_data,headers=headers)

    # 修改菜品状态信息
    def dish_update_status(self,test_data,headers):
        return requests.post(url=self.url_update_status,headers=headers)