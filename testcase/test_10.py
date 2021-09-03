# -*- coding: utf-8 -*-
"""
#----------testcase----------------
#基本信息
#Author:chen
#project：tg
"""
#提交采购任务 method=purchase.updateFormStatus

import allure
import util.globalv as gl
import json
import requests
import util.logger as ul
from data_test.axtr import ReadExtract


@allure.feature('测试用例10')
class TestProcurementType:
    def test_newly(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-10' % (self.lab)
        self.ip = gl.get_value('apiip')
        self.testplanid = gl.get_value('test_plan_id')
        self.token = gl.get_value('Cookie')
        self.formIdList = ReadExtract().read_extract()['formNum']
        print(self.formIdList)

        # 测试API地址
        self.url = '% smethod=purchase.updateFormStatus'%(self.ip)
        print(self.url)
        self.payloadData ={
                            "formIdList": [self.formIdList],
                            "action": 4,
                        }
        print(self.payloadData)

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

