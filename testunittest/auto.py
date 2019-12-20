# coding= utf-8


import unittest

from testunittest.widget import Widget


# 执行测试的类
class WidgetTestCase(unittest.TestCase):

    def setUp(self):
        self.widget = Widget()

    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40))

    def tearDown(self):
        self.widget = None

    # 构造测试集
    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(WidgetTestCase("testSize"))
        return suite


# 测试
if __name__ == "__main__":
    unittest.main(defaultTest='suite')
