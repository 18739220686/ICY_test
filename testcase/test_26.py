# -*- coding: utf-8 -*-
"""
#----------testcase----------------
#基本信息
#Author:chen
#project：tg
"""
# 获取寄售对账单 finance.getConsignmentBillList
import allure
import pytest

import util.globalv as gl
import json
import requests
import util.logger as ul


@allure.feature('测试用例26')
class TestProcurementType:
    def test_newly(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-26' % (self.lab)
        self.ip = gl.get_value('apiip')
        self.testplanid = gl.get_value('test_plan_id')
        self.token = gl.get_value('Cookie')

        # 测试API地址
        self.url = '% smethod=finance.getConsignmentBillList'% (self.ip)
        print(self.url)
        self.payloadData = {
                    "paymentNum": "",
                    "status": [],
                    "sort": "",
                    "sortType": "",
                    "page": 1,
                    "pageSize": 20
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

if __name__ == '__main__':
    pytest.main(['test_26.py'])
