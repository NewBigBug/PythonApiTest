import unittest
import requests


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
        url = "http://127.0.0.1:5000/api/users/1002"
        data = {
            'name': 'uu1',
            'password': 'uu1p'
        }
        resp = self.api_client.request(method='POST', url=url, json=data)
        print(resp.json())
        self.assertEqual(201, resp.status_code)
        self.assertEqual(True, resp.json()['success'])

    def tearDown(self):
        #self.api_client.close()
        print('tearDown')
