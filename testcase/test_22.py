# -*- coding: utf-8 -*-
"""
#----------testcase----------------
#基本信息
#Author:chen
#project：tg
"""
# AI查询全部提交供应商 /getConsignmentStatistics
import allure
import pytest

import util.globalv as gl
import json
import requests
import util.logger as ul
from data_test.axtr import Con


@allure.feature('测试用例22')
class TestProcurementType:
    def test_newly(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-22' % (self.lab)
        self.ip = gl.get_value('AIip')
        self.testplanid = gl.get_value('test_plan_id')
        self.token = gl.get_value('Cookie')
        self.appliedSupplierIds = self.id = Con().con_read()['appliedSupplierIds']
        print(self.appliedSupplierIds)

        # 测试API地址
        self.url = '% s/getConsignmentStatistics'% (self.ip)
        print(self.url)
        self.payloadData = {
                    "start": "2021-03-01",
                    "end": "2021-03-31",
                    "excludeSupplierIds": self.appliedSupplierIds
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

        # 写入至yaml文件
        res = r.json()['data']
        print(res)
        list = Con().con_write(res)  # 把字典格式的文件存入yaml文件
        print(list)

if __name__ == '__main__':
    pytest.main(['test_22.py'])
