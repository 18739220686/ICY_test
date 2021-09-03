# -*- coding: utf-8 -*-
"""
#----------testcase----------------
#基本信息
#Author:chen
#project：tg
"""
# 账号登录 /v1/user/accountLogin

import allure
import pytest
import util.globalv as gl
import json
import requests
import util.logger as ul
from data_test.axtr import Login


@allure.feature('登录')
class Test_Login:
    def test_login(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-00' % (self.lab)
        self.ip = gl.get_value('apiip')

        # 测试API地址 '% s/v1/user/accountLogin'% (self.ip)
        self.url = 'https://ssotest.icy.design/v1/user/accountLogin'
        print(self.url)
        self.payloadData = {
            "account": "COO",
            "password": "69c5fcebaa65b560eaf06c3fbeb481ae44b8d618"
        }

        self.payloadHeader = {
        }
        # 打印requests
        self.data = json.dumps(self.payloadData)
        self.headers = self.payloadHeader
        ul.log.logger.info("%s is open!~~~~~~~~~~~~~~~~~~~~~~~~~~~~" % (self.caseid))

        r = requests.request("post", url=self.url, headers=self.payloadHeader, data=self.data, verify=False)

        print(r.json())

        ul.log.logger.info(r)

        # 断言
        assert r.json()['userId'] == 0
        # assert r.json()['success'] == True
        # assert (1, r.json()['data']['success'])

        # 写入至yaml文件
        res = r.json()
        print(res)
        list = Login().token_write(res)  # 把字典格式的文件存入yaml文件
        print(list)


if __name__ == '__main__':
    pytest.main(['-vs', 'test_001_login.py'])
