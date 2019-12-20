import HTMLTestRunner
import os
import time
import unittest

from test_case import test_asset, test_qa
import sendmail

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(test_asset.Asset))
suite.addTest(unittest.makeSuite(test_qa.QA))
time.sleep(3)
now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
# suite.addTest(Testskynetcase('test_cityList'))
# suite.addTest(Testmtacase('test_deliver'))
# 定义报告路径
filename = "D:\\PycharmProjects\\skynetservicetest\\report\\" + now + 'TestReport.html'
# 定义报告文件权限，wb，表示有读写权限
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'skynet服务接口自动化测试',
    description=u'用例执行情况')
# 执行测试
runner.run(suite)
# 关闭文件，否则会无法生成文件
fp.close()


sendmail.send_mail()
