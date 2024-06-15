# 登录：
import requests
import config


# 创建接口类
class StatisticAPI:
    # 初始化
    def __init__(self):
        # 指定url基本信息
        self.url_statistic_turnover = config.BASE_URL + "/admin/report/turnoverStatistics"
        self.url_statistic_user = config.BASE_URL + "/admin/report/userStatistics"
        self.url_export = config.BASE_URL + "/admin/shop/export"


    # 营业额
    def turnoverStatistic(self, test_data,headers):
        return requests.get(url=self.url_statistic_turnover,params=test_data,headers=headers)

    # 用户
    def userStatistic(self, test_data,headers):
        return requests.get(url=self.url_statistic_user,data=test_data,headers=headers)

        # 导出
    def exportExcel(self, headers):
        return requests.put(url=self.url_export, headers=headers)

