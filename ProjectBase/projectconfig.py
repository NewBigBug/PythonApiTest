from utils import load_yaml_file


def load_testconfig():
    testconfig = load_yaml_file('../TestCase/TestData/config.yaml')
    return testconfig