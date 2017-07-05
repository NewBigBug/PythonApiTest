import os

import yaml

#加载yaml文件
def load_yaml_file(yaml_file):
    with open(yaml_file, 'r+') as stream:
        return yaml.load(stream)

#判断传入的case文件后缀名，使用对应的加载方法，目前只有yaml，暂未完成
def load_testcases(testcase_file_path):
    file_suffix = os.path.splitext(testcase_file_path)[1]
    if file_suffix in ['.yaml', '.yml']:
        return load_yaml_file(testcase_file_path)
    #elif file_suffix in ['.yaml', '.yml']:
    #    return load_yaml_file(testcase_file_path)
    else:
        # '' or other suffix
        print ("Bad testcase file name!")

#加载传入case文件夹，暂未完成
def load_foler_files(folder_path):

    file_list = []

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_list.append(file_path)

    return file_list


def load_testcases_by_path(path):
    """ load testcases from file path
    @param path
        path could be in several type:
            - absolute/relative file path
            - absolute/relative folder path
            - list/set container with file(s) and/or folder(s)
    @return testcase sets list, each testset is corresponding to a file
        [
            {"name": "desc1", "config": {}, "testcases": [testcase11, testcase12]},
            {"name": "desc2", "config": {}, "testcases": [testcase21, testcase22, testcase23]},
        ]
    """

    """
    if isinstance(path, (list, set)):
        testsets_list = []

        for file_path in set(path):
            _testsets_list = load_testcases_by_path(file_path)
            testsets_list.extend(_testsets_list)

        return testsets_list

    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)

    if os.path.isdir(path):
        files_list = load_foler_files(path)
        return load_testcases_by_path(files_list)
 
    """
    if os.path.isfile(path):
        testset = []
        try:
            testcases_list = load_testcases(path)
            print(testcases_list[0])#type=List
        except Exception:
            return []

        for item in testcases_list:

                    testset["testcases"].append(item["test"])
                    print(type(testset))

        return [testset]

    else:
        print("文件类型异常")
        return []
