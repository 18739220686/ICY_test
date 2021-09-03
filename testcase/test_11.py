# -*- coding: utf-8 -*-
"""
#----------testcase----------------
#基本信息
#Author:chen
#project：tg
"""
# 查看采购单详情 method=purchasePlan.getPurchasePlanList&storeHouseId

import allure
import util.globalv as gl
import util.test_get_post as gp
import json
import config.config
import requests
import util.logger as ul


@allure.feature('测试用例11')
class TestProcurementType:
    def test_newly(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-11' % (self.lab)
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

        print(r.json())
        ul.log.logger.info(r)

        # 断言
        assert r.json()['result'] == 0
