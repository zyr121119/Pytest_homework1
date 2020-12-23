import pytest
import yaml
import os
from pythoncode.calculator import Calculator

path= os.getcwd()+"./data.yaml"
def getyaml(name:str):
    with open(path) as f:
        datas = yaml.safe_load(f)
        nums = datas[name]['nums']
        ids = datas[name]['ids']
    return [nums,ids]

@pytest.fixture(scope="module")
def get_cal():
    print("获取计算器实例")
    print("开始测试")
    cal = Calculator()
    yield cal
    print("结束测试")

@pytest.fixture(params=getyaml("add")[0],ids=getyaml("add")[1],scope="module")
def get_adddata(request):
    print("开始计算")
    adddata = request.param
    yield adddata
    print("结束计算")


@pytest.fixture(params=getyaml("sub")[0],ids=getyaml("sub")[1],scope="module")
def get_subdata(request):
    print("开始计算")
    subdata = request.param
    yield subdata
    print("结束计算")

@pytest.fixture(params=getyaml("mul")[0],ids=getyaml("mul")[1],scope="module")
def get_muldata(request):
    print("开始计算")
    muldata = request.param
    yield muldata
    print("结束计算")

@pytest.fixture(params=getyaml("div")[0],ids=getyaml("div")[1],scope="module")
def get_divdata(request):
    print("开始计算")
    divdata = request.param
    yield divdata
    print("结束计算")


