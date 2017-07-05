import unittest
import requests

"""
requests库的session对象能够帮我们跨请求保持某些参数，也会在同一个session实例发出的所有请求之间保持cookies。
"""
class ServerTest(unittest.TestCase):
    def setUp(self):
        self.host = "http://127.0.0.1:5000"
        self.api_client = requests.Session()
        print('setUp')


    def test_clear_user(self):
        url = "%s/api/users" % (self.host)
        resp = self.api_client.delete(url)
        print(resp.json())
        self.assertEqual(True, resp.json()['success'])


    def test_creatuser(self):
        url = "%s/api/users/%d" % (self.host, 10001)
        data = {
            'name': 'uu1',
            'password': 'uu1p'
        }
        resp = self.api_client.post(url, json=data)
        print(resp.json())
        self.assertEqual(201, resp.status_code)
        self.assertEqual(True, resp.json()['success'])

    def tearDown(self):
        self.api_client.close()
        print('tearDown')

