# encoding: utf-8
import unittest
from data import data_info
import requests


class QA(unittest.TestCase):

    def setUp(self):
        pass

    def test_List(self):
        url = data_info.url + data_info.List
        response = requests.get(url)
        print(url)
        print(response.text)

    def test_cityList(self):
        url = data_info.url + data_info.cityList
        params =''
        #params = 'department='
        response = requests.get(url, params)
        print(url)
        print(response.text)
        self.assertEqual(100, response.json()['error_code'])

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
