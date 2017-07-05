import requests
import projectconfig
import utils




def case_generator(i, host, testcase):
    case_config=projectconfig.load_testconfig()
    config_path=case_config['casefile']
    caselibrary=utils.load_case_by_path(config_path)
    for key in caselibrary.items():
        pathname=str(key)
        testcases=caselibrary[key]
        for i in range(len(testcases)):
            caseresult=flask_casebase.case_generator(i, self.host, testcases[i])
            msg=flask_casebase.case_result(testcase_file_path, caseresult)
            print(msg)

        api_client = requests.request
        case_name = testcase['name']
        req_kwargs = testcase['request']
        check_point = testcase['Checkpoint']
        url = host + req_kwargs.pop('url')
        method = req_kwargs.pop('method')
        resp_obj = api_client(method, url, **req_kwargs)
         result = utils.assertresult(resp_obj, check_point)
    resultmsg = {
        'CaseNumb': i,
        'CaseName': case_name,
        'AsertMsg': result
    }
    return resultmsg


def case_result(filename, resultmsg):
    rmg = 'CasePath：' + str(filename)
    for key, value in resultmsg.items():
        rmg = rmg + '\n' + str(key) + ':' + str(value)
    return rmg
