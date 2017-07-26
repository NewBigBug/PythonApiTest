# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 15:27
# @Author  : Charles
# @File    : test_UserParam.py
# @Software: PyCharm


import unittest
import UserParam
import DataGenerate


class Test_UsrPara(unittest.TestCase):

    def test_sign_generate(self):

        datadic = 'APP_KEY10001DEVICE_VERSION112FORMATjsonID_NO659004196004172187MEDIA_DATA[{"MEDIA":"","MEDIA_TYPE":1},{"MEDIA":"","MEDIA_TYPE":2}]MOBILE15502168672NAMEreterteTIMESTAMP2017-07-26 09:59:51U_IDv-yunliuVERSION1.0'

        secret='B4B83DC748B8E511A2846C0B840997C3'

        cc=UserParam.sign_generate_01(datadic, secret)
        print(cc)

    """
    def test_01(self):

        up = UserParam.param_generate()

        datadic = {'Request_Body': {
            'name': {'name1': {'name2': {'name3': '3432fdf$sign$'}}},
            'password': 'wdsfsdfsdfsdfsdfrrwerewew$tm$'
        }
        }

        cc = DataGenerate.data_generate(datadic, up)
        print(cc)
    
    """