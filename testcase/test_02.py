# -*- coding: utf-8 -*-
"""
#----------testcase----------------
#基本信息
#Author:chen
#project：tg
"""
# 新增采购计划列表 method=purchasePlan.updatePurchasePlan

import pytest
import util.globalv as gl
import util.test_get_post as gp
import json
import config.config
import util.logger as ul
import requests


class TestNewSuppliers:
    def test_newly(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-02' % (self.lab)
        self.ip = gl.get_value('apiip')
        self.testplanid = gl.get_value('test_plan_id')
        self.token = gl.get_value('Cookie')

        # 测试API地址
        self.url = '% smethod=purchasePlan.updatePurchasePlan'% (self.ip)
        print(self.url)
        self.payloadData ={
                                "purchaseGenreId": 1,
                                "storeHouseId": 3,
                                "originPurchaseNum": "",
                                "remark": "巴拉巴拉吧",
                                "goodsList": [{
                                    "operateArriveDate": "2021-03-11",
                                    "skuId": "1553253210",
                                    "writeOffPrice": 0,
                                    "purchaseCount": 50,
                                    "totalFaxAmount": 0
                                }, {
                                    "operateArriveDate": "2021-03-11",
                                    "skuId": "1559253210",
                                    "writeOffPrice": 0,
                                    "purchaseCount": 60,
                                    "totalFaxAmount": 0
                                }]
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
    pytest.main(['-vs', 'test_02.py'])