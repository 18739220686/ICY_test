# -*- coding: utf-8 -*-
"""
#----------testcase----------------
#基本信息
#Author:chen
#project：tg
"""
# 获取分配采购列表 method=purchasePlan.getPurchasePlanList&storeHouseId=&barcode=
import allure

import util.globalv as gl
import json
import requests
import util.logger as ul
from data_test.axtr import ReadExtract


@allure.feature('测试用例6')
class TestProcurementType:
    def test_newly(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-06' % (self.lab)
        self.ip = gl.get_value('apiip')
        self.testplanid = gl.get_value('test_plan_id')
        self.token = gl.get_value('Cookie')

        # 测试API地址
        self.url = '% smethod=purchasePlan.getPurchasePlanList&storeHouseId=&barcode=&page=1&pageSize=10&status=1'% (self.ip)
        print(self.url)
        self.payloadData ={

                        }

        self.payloadHeader = {
            'Content-Type': "application/json",
            'Cookie': self.token
        }
        #打印requests
        self.data = json.dumps(self.payloadData)
        self.headers = self.payloadHeader
        ul.log.logger.info("%s is open!~~~~~~~~~~~~~~~~~~~~~~~~~~~~" % (self.caseid))

        r = requests.request("get", url=self.url, headers=self.payloadHeader, data=self.data,verify=False)

        # 写入至yaml文件
        res = r.json()['data']['list'][0]
        print(res)
        list = ReadExtract().write_extract(res)  # 把字典格式的文件存入yaml文件
        print(list)


        print(r.json()['data'])
        ul.log.logger.info(r)

        # 断言
        assert r.json()['result'] == 0

