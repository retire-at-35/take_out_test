import os
import yaml

import config


class YamlUtil:
    #读取yaml文件
    def read_extract_yaml(self,key):
        with open(config.BASE_PATH+'/extract.yml',mode='r',encoding='utf-8') as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value[key]

    #写入yaml文件
    def write_extract_yaml(self,data):
        with open(config.BASE_PATH+'/extract.yml',mode='w',encoding='utf-8') as f:
            yaml.dump(data,stream=f,allow_unicode=True)


