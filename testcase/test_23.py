# -*- coding: utf-8 -*-
"""
#----------testcase----------------
#基本信息
#Author:chen
#project：tg
"""
# 提交寄售仅保存 finance.updateConsignmentPaymentForm
import allure
import pytest
import util.globalv as gl
import json
import requests
import util.logger as ul
from data_test.axtr import Con


@allure.feature('测试用例23')
class TestProcurementType:
    def test_newly(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-23' % (self.lab)
        self.ip = gl.get_value('apiip')
        self.testplanid = gl.get_value('test_plan_id')
        self.token = gl.get_value('Cookie')
        self.supplierIds = self.id = Con().con_read()['supplyId']
        print(self.supplierIds)

        # 测试API地址
        self.url = '% smethod=finance.updateConsignmentPaymentForm'% (self.ip)
        print(self.url)
        self.payloadData ={
                            "supplierIds": [self.supplierIds],
                            "month": "2021-03",
                            "remark": "",
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
    pytest.main(['test_23.py'])
