# -*- coding: utf-8 -*-
"""
#----------testcase----------------
#基本信息
#Author:chen
#project：tg
"""
# 筛选已支付供应商 finance.getAppliedSupplierIds
import allure
import pytest

import util.globalv as gl
import json
import requests
import util.logger as ul
from data_test.axtr import Con


@allure.feature('测试用例21')
class TestProcurementType:
    def test_newly(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-21' % (self.lab)
        self.ip = gl.get_value('apiip')
        self.testplanid = gl.get_value('test_plan_id')
        self.token = gl.get_value('Cookie')

        # 测试API地址
        self.url = '% smethod=finance.getAppliedSupplierIds'% (self.ip)
        print(self.url)
        self.payloadData ={
                    "month": "2021-03"
                }

        self.payloadHeader = {
            'Content-Type': "application/json",
            'Cookie': self.token
        }
        #打印requests
        self.data = json.dumps(self.payloadData)
        self.headers = self.payloadHeader
        ul.log.logger.info("%s is open!~~~~~~~~~~~~~~~~~~~~~~~~~~~~" % (self.caseid))

        r = requests.request("post", url=self.url, headers=self.payloadHeader, data=self.data,verify=False)

        print(r.json())
        ul.log.logger.info(r)

        # 断言
        assert r.json()['result'] == 0

        # 写入至yaml文件
        res = r.json()['data']
        print(res)
        data = Con().con_write(res)  # 把字典格式的文件存入yaml文件
        print(data)

if __name__ == '__main__':
    pytest.main(['test_21.py'])
