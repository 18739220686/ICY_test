# -*- coding: utf-8 -*-
"""
#----------testcase----------------
#基本信息
#Author:chen
#project：tg
"""
# 获取采购计划列表 method=purchasePlan.getPurchasePlanList

import allure
import pytest
import util.globalv as gl
import util.test_get_post as gp
import json
import config.config
import requests
import util.logger as ul
import util.reporyresult as cr
import modulefinder


class Test_UpdateRate:
    # 参数化
    # @pytest.mark.parametrize('rate,description,status', [['111', '测试2', '1'], ['222', '测试3', '0']])
    def test_Tax(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-01' % (self.lab)
        self.ip = gl.get_value('apiip')
        self.testplanid = gl.get_value('test_plan_id')
        self.token = gl.get_value('Cookie')
        print(self.token)

        # 测试API地址
        self.url = '% smethod=purchasePlan.getPurchasePlanList' % (self.ip)
        print(self.url)
        self.payloadData = {
            "barcode": "",
            "storeHouseId": "",
            "status": 1,
            "bandId": "",
            "purchaseTypeId": [],
            "purchaseGenreId": [],
            "sort": "",
            "sortType": "",
            "page": 1,
            "pageSize": 20
        }

        self.payloadHeader = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cookie': self.token
        }

        # 打印requests
        self.data = json.dumps(self.payloadData)
        self.headers = self.payloadHeader
        ul.log.logger.info("%s is open!~~~~~~~~~~~~~~~~~~~~~~~~~~~~" % (self.caseid))

        r = requests.request('post', url=self.url, headers=self.payloadHeader, data=self.data, verify=False)

        print(r.json())
        ul.log.logger.info(r)

        # 断言
        assert r.json()['result'] == 0


if __name__ == '__main__':
    pytest.main(['test_01.py'])
