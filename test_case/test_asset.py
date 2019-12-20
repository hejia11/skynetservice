# encoding: utf-8
import unittest
from data import data_info
import requests


class Asset(unittest.TestCase):

    def test_List(self):
        u"""获取大区列表"""
        url = data_info.url + data_info.List
        response = requests.get(url)
        print(url)
        print(response.text)

    def test_cityList(self):
        u"""获取大区下的城市列表"""
        url = data_info.url + data_info.cityList
        params = 'department=98'
        response = requests.get(url, params)
        print(url)
        print(response.text)

    def test_creat(self):
        url = "http://47.96.53.33/swagger-apiui/skynet-service/shop-asset/create"
        params = {
            "operatorKey": "2221",
            "name": "测试门店1220",
            "openDt": "2019-12-03  00:00:00",
            "locationId": 126,
            "projectLeaderId": 2221,
            "projectLeaderName": "何佳",
            "shopContract": {
                "partnerCompany": "测试12",
                "partnerRepresentative": "测试12",
                "partnerPhone": "021-12345677",
                "ahsCompany": "上海悦亿网络科技有限公司",
                "ahsRepresentative": "徐迅徐迅",
                "responsibilityOfBreach": "徐迅徐迅徐迅111",
                "fileUrls": [
                    "https://aihuishou-internal.oss-cn-hangzhou.aliyuncs.com/asset_contract_attachment/499-appliedMTU3MjUyMjk0MDIxMQ==.png"
                ],
                "rentPerMonth": 200,
                "rentTaxRate": 10,
                "rentFreeDays": 10,
                "deposit": 1000,
                "propertyFeePerMonth": 400,
                "propertyFeeTaxRate": 2,
                "promotionFeePerMonth": 400,
                "paymentCycle": 1,
                "invoiceType": 1,
                "actualGain": 0,
                "originalLease": "37 个月 26 天",
                "rentTotalAmount": 7506.67,
                "endDt": "2022-12-10 00:00:00",
                "beginDt": "2019-10-31 00:00:00",
                "monthlyPayDay": 3,
                "initialPaymentToDate": "2019-09-01 00:00:00",
                "accountCreateModels": [
                    {
                        "type": 1,
                        "bankName": "上海银行",
                        "accountNo": "6222222222222222",
                        "accountName": "徐迅"
                    }
                ],
                "name": "徐迅",
                "remark": "徐迅",
                "billEndDate": "2023-01-01 00:00:00",
                "billBeginDate": "2019-10-01 00:00:00",
                "finalPaymentNoticeDate": "2019-12-04 00:00:00",
                #"id": 73
            },
            "id": 65
        }
        r1 = requests.post(url, json=params)
        print(r1.text)


if __name__ == '__main__':
    unittest.main()
    '''suite = unittest.TestSuite()
    suite.addTest(Testskynetcase('test_List'))
    time.sleep(3)
    suite.addTest(Testskynetcase('test_cityList'))
    # suite.addTest(Testmtacase('test_deliver'))
    # 定义报告路径
    filename = 'TestReport.html'
    # 定义报告文件权限，wb，表示有读写权限
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'资产门店接口自动化测试',
        description=u'用例执行情况')
    # 执行测试
    runner.run(suite)
    # 关闭文件，否则会无法生成文件
    fp.close()
    send_mail()'''
