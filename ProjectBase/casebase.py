import requests
import projectconfig
import utils


def case_requests(method, url, **req_kwargs):
    api_client = requests.request
    resp_obj = api_client(method, url, **req_kwargs)
    return resp_obj


def case_result(case_result_list):
    rmg = ''
    for i in range(len(case_result_list)):
        for key, value in case_result_list[i].items():
            rmg = rmg + str(key) + ':' + str(value) + '\n'
    return rmg


def case_generator_request():
    case_result_list=[]
    case_config = projectconfig.load_testconfig()
    config_path = case_config['casefile']
    url_host = case_config['host']
    caselibrary = utils.load_case_by_path(config_path)
    for key, value in caselibrary.items():
        file_path = str(key)
        test_case = value
        for i in range(len(test_case)):
            testcase = test_case[i]
            case_path = file_path
            case_name = testcase['name']
            req_kwargs = testcase['request']
            url = url_host + req_kwargs.pop('url')
            method = req_kwargs.pop('method')
            check_point = testcase['Checkpoint']
            resp_obj = case_requests(method, url, **req_kwargs)
            result = utils.assertresult(resp_obj, check_point)
            msg = {
                'CasePath': case_path,
                'CaseNumb': i,
                'CaseName': case_name,
                'AsertMsg': result
            }
            case_result_list.append(msg)
    return case_result_list



