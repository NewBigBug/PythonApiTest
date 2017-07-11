
import os
import xlrd as xlrd
import yaml
import logmsg
from exception import ParamsError


# 加载yaml
def load_yaml_file(yaml_file):
    with open(yaml_file, 'r') as stream:
        return yaml.load(stream)


# 加载excel
def load_excel_file(excel_file):
    with xlrd.open_workbook(excel_file) as stream:
        return stream


# 加载传入yamlcase文件夹
def load_foler_files(folder_path):
    file_list = []

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_list.append(file_path)

    return file_list


# 根据传入的路径类型处理用例文件，文件夹(仅支持yaml)/单个文件,同时将filepaht作为key，用例内容dict作为value，返回值为dict
# 如果文件为excel，会有存在多个sheet页测试数据的情况，每个sheet页做一个键值对
def load_case_by_path(path):

    file_casedict = {}

    if os.path.isdir(path):
        casefile_list = load_foler_files(path)
        for i in range(len(casefile_list)):
            file_casedict[casefile_list[i]] = load_yaml_file(casefile_list[i])
        return file_casedict

    if os.path.isfile(path):
        file_suffix = os.path.splitext(path)[1]
        if file_suffix in ['.yaml', '.yml']:
            file_casedict[path] = load_yaml_file(path)
        elif file_suffix in ['.xlsx', '.xls']:
            xlrd_stream = load_excel_file(path)

            case_lines={}
            for i in range(len(xlrd_stream.sheets())):
                sheetname = xlrd_stream.sheet_by_index(i).name
                taledata = xlrd_stream.sheet_by_index(i)

                case_line_no = {}
                for j in range(1, taledata.nrows):

                    case_line = {
                                'API_Purpose': taledata.cell(j, 1).value.replace('\n', '').replace('\r', ''),
                                'Request_Url': taledata.cell(j, 2).value.replace('\n', '').replace('\r', ''),
                                'Request_method': taledata.cell(j, 3).value.replace('\n', '').replace('\r', ''),
                                'Header': taledata.cell(j, 4).value.replace('\n', '').replace('\r', ''),
                                'Body_Type': taledata.cell(j, 5).value.replace('\n', '').replace('\r', ''),
                                'Request_Body': taledata.cell(j, 6).value.replace('\n', '').replace('\r', ''),
                                'Need_Cookie': taledata.cell(j, 7),
                                'Need_Sign': taledata.cell(j, 8),
                                'Need_Collection': taledata.cell(j, 9),
                                'Depends': taledata.cell(j, 10).value.replace('\n', '').replace('\r', ''),
                                'Response_Type': taledata.cell(j, 11).value.replace('\n', '').replace('\r', ''),
                                'Checkpoint': taledata.cell(j, 12).value.replace('\n', '').replace('\r', ''),
                                'Active': taledata.cell(j, 13)
                    }
                    case_line_no['No.'+str(j)] = case_line
                case_lines[path+'_'+sheetname] = case_line_no
            return case_lines
        else:
            logmsg.logger.error(path + '用例文件格式不正确！')

        return file_casedict

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
