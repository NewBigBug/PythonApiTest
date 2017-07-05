import requests

import utils


def case_generator(i, host, testcase):
    api_client = requests.request
    case_name = testcase['name']
    req_kwargs = testcase['request']
    check_point = testcase['Checkpoint']
    url = host + req_kwargs.pop('url')
    method = req_kwargs.pop('method')
    resp_obj = api_client(method, url, **req_kwargs)
    result = utils.assertresult(resp_obj, check_point)
    resultmsg={
        'CaseNumb': i,
        'CaseName': case_name,
        'AsertMsg': result
    }
    return resultmsg


def case_result(resultmsg):
    rmg = ''
    for key, value in resultmsg.items():
        rmg = rmg+'\n'+str(key)+':'+str(value)
    return rmg