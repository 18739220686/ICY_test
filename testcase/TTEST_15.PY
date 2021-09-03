# -*- coding: utf-8 -*-
"""
#----------testcase----------------
#基本信息
#Author:chen
#project：tg
"""
# 预付款银行卡付款 method=finance.createPurchasePayment

import allure
import util.globalv as gl
import util.test_get_post as gp
import json
import config.config
import requests
import util.logger as ul


@allure.feature('测试用例15')
class TestProcurementType:
    def test_newly(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-15' % (self.lab)
        self.ip = gl.get_value('apiip')
        self.testplanid = gl.get_value('test_plan_id')
        self.token = gl.get_value('Cookie')

        # 测试API地址
        self.url = '% smethod=finance.createPurchasePayment'% (self.ip)
        print(self.url)
        self.payloadData ={
                            "purchaseId": 1556274479,
                            "supplierName": "花数果（wxn测试）",
                            "bank": "工商银行",
                            "account": "777777777777771",
                            "stage": 1,
                            "purchaseAmount": 13000,
                            "amount": 7800,
                            "payStyle": "6:2:2",
                            "goodsList": [],
                            "contents": [{
                                "status": 1,
                                "disable": False,
                                "amount": 7800
                            }, {
                                "status": 2,
                                "disable": False,
                                "amount": 2600,
                                "goodsList": [{
                                    "skuId": "1552935991",
                                    "spuId": "1540308832",
                                    "sku": "2051F00061W402",
                                    "spu": "2051F00061",
                                    "name": "春2051F00061",
                                    "count": 6,
                                    "actualPrice": 1000,
                                    "remainCount": 6
                                }, {
                                    "skuId": "1552936003",
                                    "spuId": "1540308827",
                                    "sku": "20510H0056W482",
                                    "spu": "20510H0056",
                                    "name": "summer20510H0056",
                                    "count": 7,
                                    "actualPrice": 1000,
                                    "remainCount": 7
                                }]
                            }, {
                                "status": 3,
                                "disable": False,
                                "amount": 0
                            }],
                            "style": 4
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
