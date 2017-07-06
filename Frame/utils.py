import os
# 加载yaml文件
import yaml
from termcolor import colored

from exception import ParamsError


def load_yaml_file(yaml_file):
    with open(yaml_file, 'r') as stream:
        return yaml.load(stream)


# 判断传入的case文件后缀名，使用对应的加载方法，目前只有yaml，暂未完成
def load_case_file(testcase_file_path):
    file_suffix = os.path.splitext(testcase_file_path)[1]
    if file_suffix in ['.yaml', '.yml']:
        return load_yaml_file(testcase_file_path)
    else:
        print("Bad testcase file name!")


# 加载传入case文件夹
def load_foler_files(folder_path):
    file_list = []

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_list.append(file_path)

    return file_list


def load_caseset(singlefilepath):
    testset = []
    try:
        testcases_list = load_case_file(singlefilepath)

    except ParamsError:
        return

    for key in testcases_list:
        testset.append(testcases_list[key])

    return testset


def load_case_by_path(path):
    testset_isfile = {}
    if os.path.isdir(path):

        casefile_list = load_foler_files(path)
        for i in range(len(casefile_list)):
            testset_isfile[casefile_list[i]] = load_caseset(casefile_list[i])
        return testset_isfile

    if os.path.isfile(path):
        testset_isfile = {
            path: load_caseset(path)
        }

        return testset_isfile

    else:
        print("传入文件路径异常：" + path)
        return


def assertresult(resp, checkpoint):
    json_diff = {}

    respjson = resp.json()
    for key, point in checkpoint.items():
        if key in respjson:
            resppame = respjson[key]
            if str(resppame) != str(point):
                json_diff[key] = {
                    'respdata': resppame,
                    'checkdata': point,
                    'checkresult': False
                }
            else:
                json_diff[key] = {
                    'respdata': resppame,
                    'checkdata': point,
                    'checkresult': True
                }
        else:
            json_diff[key] = {
                'checkdata': point,
                'checkresult': 'Checkpoint is not exist!'
            }

    return json_diff

"""
def assertresult_tostr(json_diff):
    assertstr = ''
    for key, value in json_diff.items():
        assertstr = assertstr + str(key) + ':' + str(value)
    if not json_diff['checkresult']:
        assertresultstr = colored(assertstr, 'red')
    return assertresultstr
"""