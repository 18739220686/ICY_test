# -*- coding: utf-8 -*-
"""
#----------testcase----------------
#基本信息
#Author:chen
#project：tg
"""
#创建采购任务 method=purchase.updatePurchaseForm

import allure
import util.globalv as gl
import json
import requests
import util.logger as ul
from data_test.axtr import ReadExtract




@allure.feature('测试用例9')
class TestProcurementType:
    def test_newly(self):
        self.lab = gl.get_value('lab')
        self.caseid = '%s-09' % (self.lab)
        self.ip = gl.get_value('apiip')
        self.testplanid = gl.get_value('test_plan_id')
        self.token = gl.get_value('Cookie')
        self.id = ReadExtract().read_extract()['id']
        self.merchandiserId = ReadExtract().read_extract()['merchandiserId']
        print(self.id)

        # 测试API地址
        self.url = '% smethod=purchase.updatePurchaseForm'% (self.ip)
        print(self.url)
        self.payloadData ={
                            "supplierId":1539844984,
                            "supplierName":"ODM类型测试供应商",
                            "merchandiserId": self.merchandiserId,
                            "onNewSample":0,
                            "purchaseTypeName":"ODM",
                            "remark":"",
                            "purchaseTypeId":1547608649,
                            "settlementCycleId":1547605853,
                            "settlementCycleName":"3/6/1",
                            "taxRateId":1547603037,
                            "taxRateName":"13",
                            "merchandiserName":"供应链老大",
                            "goodsList":[
                                {
                                    "id":self.id,
                                    "name":"测试-测试商品",
                                    "imgList":[
                                        "ai-admin/1ab5404172d424aa2f1cfc1696fb1695.jpg"
                                    ],
                                    "img":"ai-admin/1ab5404172d424aa2f1cfc1696fb1695.jpg",
                                    "colorName":"中灰",
                                    "spuBarcode":"19160A0011",
                                    "skuBarcode": "1922A10009W703",
                                    "unitName":"件",
                                    "writeOffPrice":"",
                                    "hangTagPrice":"3242.00",
                                    "sizeName":"M",
                                    "sizeAndColor":"中灰 ,M",
                                    "saleChannelName":"电商销售",
                                    "purchaseGenreName":"首单",
                                    "bandName":"",
                                    "purchaseTypeName":"只拿",
                                    "storeHouseName":"研发测试仓",
                                    "storeHouseId":3,
                                    "isOre":0,
                                    "purchaseCount":60,
                                    "onlineCount":0,
                                    "offlineCount":0,
                                    "supplierId":1539844984,
                                    "supplierName":"ODM类型测试供应商",
                                    "merchandiserId":1607068302,
                                    "merchandiserName":"供应链老大",
                                    "arriveCount":0,
                                    "offlineAndOnlineCount":"0/0",
                                    "oreArriveCount":"0/0",
                                    "offlineAndOnlineArriveCount":"0/0",
                                    "bandArriveDate":"2021-03-11",
                                    "creator":"COO",
                                    "createTime":"2021-03-08",
                                    "remark":"巴拉巴拉吧",
                                    "status":1,
                                    "estimatedPurchaseAmount":"0.0000",
                                    "image":"ai-admin/1ab5404172d424aa2f1cfc1696fb1695.jpg",
                                    "unitPrice":"222.0000",
                                    "totalAmount":"13320.00",
                                    "operateArriveDate":"2021-03-08T16:00:00.000Z"
                                }
                            ],
                            "isOre":1,
                            "storeHouseId":3
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
        list = ReadExtract().write_extract(res)  # 把字典格式的文件存入yaml文件
        print(list)

        # 断言
        assert r.json()['result'] == 0