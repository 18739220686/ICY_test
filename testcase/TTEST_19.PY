# -*- coding: utf-8 -*-
"""
#----------testcase----------------
#基本信息
#Author:chen
#project：tg
"""
# 采购付款-确认付款 method=finance.confirmPayment
import allure
import util.globalv as gl
import util.test_get_post as gp
import json
import config.config
import requests
import util.logger as ul


@allure.feature('测试用例19')
class TestProcurementType:
    def test_newly(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-19' % (self.lab)
        self.ip = gl.get_value('apiip')
        self.testplanid = gl.get_value('test_plan_id')
        self.token = gl.get_value('Cookie')

        # 测试API地址
        self.url = '% smethod=finance.confirmPayment'% (self.ip)
        print(self.url)
        self.payloadData ={
                                "style": 1,
                                "code": 202103080021,
                                "hasInvoice": True,
                                "invoiceCode": "111111",
                                "amount": "500",
                                "remark": ""
                            }

        self.payloadHeader = {
            'Content-Type': "application/json",
            'Cookie': self.token
        }
        #打印requests
        self.data = json.dumps(self.payloadData)
        self.headers = self.payloadHeader
        ul.log.logger.info("%s is open!~~~~~~~~~~~~~~~~~~~~~~~~~~~~" % (self.caseid))

        r = requests.request("POST", url=self.url, headers=self.payloadHeader, data=self.data,verify=False)

        print(r.json())
        ul.log.logger.info(r)

        # 断言
        assert r.json()['result'] == 0
        #assert r.json()['data']['supplierId'] == '1539844984'
