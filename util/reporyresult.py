#!/usr/bin/python
# -*- coding: utf-8 -*-
import testlink
import util.globalv as gl
import config.config

#解决连接https问题
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# 连接test link
#url = 'http://192.168.68.21/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
#key = '8980b568ad1249e102ce3962a799f742'

# url = "https://testlink.thiztech.com/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
# key = "34c3194c732457cca2f5b0bfad8b72fe"

url = gl.get_value('url')
key = gl.get_value('key')

tlc = testlink.TestlinkAPIClient(url, key)

def report_test_result(test_plan_id, test_case_id, test_result):
    tlc.reportTCResult(None, test_plan_id, None, test_result, "", guess=True,
                       testcaseexternalid=test_case_id, platformname="0")

# report_test_result("418","jft-1","f")
# report_test_result("1487","tspauto-1","p")