import os
import unittest

import yaml

import FileController


class UtilsTest(unittest.TestCase):
    """
    def test_load_testcasesfile(self):

        # absolute file path
        path = '..\TestCase\TestData\demo1.yaml'
        testset_list = utils.load_testcasesfile(path)
        test1=testset_list['test1']

        #print(type(test1))
        #print(test1['name'])


    def test_load_testcases_by_path_foler(self):

        path = '..\TestCase\TestData'
        testset_list = utils.load_case_by_path(path)
        #test1 = testset_list[1]

        #print(type(test1))
        print(testset_list)




    def test_load_case_file(self):
        path = '..\TestCase\TestData\case.yaml'

        test1 = utils.load_case_file(path)

        # print(type(test1))
        print(type(test1))
        print(test1['No.2'])

    def test_load_testcases_by_path_file_yaml(self):

        path = '..\TestCase\TestData\case.yaml'
        testset_list = FileController.load_case_by_path(path)
        #test1 = testset_list[1]

        #print(type(test1))
        print(testset_list)
        d1=testset_list['..\\TestCase\\TestData\\case.yaml']['No.1']
        print(type(d1['Active']))




    def test_load_testcases_by_path_file_excel(self):

        path = '..\TestCase\TestData\case.xlsx'
        testset_list = FileController.load_case_by_path(path)
        #test1 = testset_list[1]
        d2 = testset_list['..\\TestCase\\TestData\\case.xlsx_case']['No.1']
        print(testset_list)
        print(type(d2['Active']))


    def test_create_yaml_file(self):
        case_info = {
            '/api/login': 'PASS'
        }

        path='D:\GitPro\Python\PythonApiTest\output\\tempyaml.yaml'

        if os.path.exists(path):
            os.remove(path)
            createstream = FileController.create_yaml_file(path)
        else:
            createstream = FileController.create_yaml_file(path)

        #yaml.dump(case_info, createstream)
        #createstream.close()

        rd=FileController.write_yaml_file(case_info,path)

        #ss=rd['/api/login']
        #print(ss)



    def test_list_all_dict(self):
        dictjson =
            'BODY': '{"RESULT":true,"MESSAGE":"登录成功","MODEL":{"ID":1196,"NAME":"魏双双","TELPHONE":"15502168672","CREATED_TIME":"2017-06-19 09:53:38","CITY":"QuarkFinance","ID_NO":"41152119910617391X","STAFF_NO":"2016050301","IS_SET_GESTURE_PASSWORD":true,"IS_SIGN_IN":false,"PHONE_OS":0,"DEPARTMENT_NAME":"技术部","USER_ACCOUNT_DEPARTMENT_ID":"83","USER_COMPANY_ID":"323ea269-5aea-4f60-b6d8-31d3215e208d","USER_ACCOUNT":"shuangshuangwei","IS_ACTIVED":1,"AGREEMENT_ON_CONFIDENTIALITY":"Y"}}',
            'RESPONSE_STATUS': 'OK', 'ELAPSE_TIME': '', 'ERROR_CODE': None, 'ERROR_MESSAGE': None}
    """