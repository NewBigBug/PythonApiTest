import os

import yaml

#加载yaml文件
from exception import ParamsError


def load_yaml_file(yaml_file):
    with open(yaml_file, 'r') as stream:
        return yaml.load(stream)

#判断传入的case文件后缀名，使用对应的加载方法，目前只有yaml，暂未完成
def load_case_file(testcase_file_path):
    file_suffix = os.path.splitext(testcase_file_path)[1]
    if file_suffix in ['.yaml', '.yml']:
        return load_yaml_file(testcase_file_path)
    #elif file_suffix in ['.yaml', '.yml']:
    #    return load_yaml_file(testcase_file_path)
    else:
        # '' or other suffix
        print("Bad testcase file name!")

#加载传入case文件夹
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

        casefile_list=load_foler_files(path)
        for key in casefile_list.items():
            testset_isfile={
                'filepath': key,
                'filecase': load_caseset(casefile_list)
            }

        return testset_isfile

    if os.path.isfile(path):
        testset_isfile = {
            'filepath': path,
            'filecase': load_caseset(path)
        }

        return testset_isfile

    else:
        print("文件类型异常")
        return



def assertresult(resp, checkpoint):
    json_diff = {}

    respjson=resp.json()
    for key, point in checkpoint.items():
        if key in respjson:
            resppame = respjson[key]
            if str(resppame) != str(point):
                json_diff[key]={
                    'respdata': resppame,
                    'checkdata': point,
                    'checkresult': False
                }
            else:
                json_diff[key]={
                    'checkresult': True
                }
        else:
            json_diff[key] = {
                'caseresult': 'Checkpoint 在返回值中不存在，请检查'
            }


    return json_diff



