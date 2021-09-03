
'''
-s 表示输出调试信息
-v 显示更详细的信息
-vs 显示调试详细信息
-(['-vs','文件']) 指定文件
-(['-vs','目录']) 指定目录
-n 
--reruns=次数 用例失败重跑
-x 一个错误用例停止运行
-maxfail = 2出现两个用例失败停止
-k 根据某个字段运行
@ pytest.mark.run(order=顺序)安装pytest-ordering
'''
import pytest
import os
# 忽略requests证书警告
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if __name__ == '__main__':
    '''
        allure generate 语法
        ./temp 临时报告
        -o 输出
        --clean 覆盖
        '''
    pytest.main()
    os.system('allure generate ./temp -o ./report --clean')




    # # 用例路径
    # case_path = os.path.join(os.getcwd(), "case")
    # # 报告存放路径
    # report_path = os.path.join(os.getcwd(), "report")
    # report_abspath = os.path.join(report_path, "result.html")
    # fp = open(report_abspath, "wb")
    # runner = uh.HTMLTestRunner(stream=fp,
    #                                                                        title=u'自动化测试报告,测试结果如下：',
    #                                                                        description=u'用例执行情况：')




