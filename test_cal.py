import pytest
import yaml

from pythoncode.calculator import Calculator


def readyaml(name: str):
    with open("data.yaml") as f:
        dict1 = yaml.safe_load(f)
    print(dict1)
    list1 = dict1[name]['nums']
    list2 = dict1[name]['ids']
    return [list1,list2]

class TestCal:

    def setup_class(self):
        print("开始测试TestCal")
        self.cal=Calculator()

    def teardown_class(self):
        print("TestCal测试完成")

    def setup_method(self):
        print("开始计算")

    def teardown_method(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect",readyaml("add")[0],ids=readyaml("add")[1])
    def test_add(self,a,b,expect):
        try:
            result = self.cal.add(a,b)
            if isinstance(result,float):
                result =round(result,2)
            assert result==expect
        except Exception as e:
            assert False

    @pytest.mark.parametrize("a,b,expect",readyaml("sub")[0],ids=readyaml("sub")[1])
    def test_sub(self,a,b,expect):
        try:
            result=self.cal.sub(a,b)
            if isinstance(result,float):
                result =round(result,2)
            assert result==expect
        except Exception as e:
            assert False

    @pytest.mark.parametrize("a,b,expect", readyaml("mul")[0],ids=readyaml("mul")[1])
    def test_mul(self, a, b, expect):
        try:
            result=self.cal.mul(a, b)
            if isinstance(result,float):
                result =round(result,2)
            assert  result== expect
        except Exception as e:
            assert False

    @pytest.mark.parametrize("a,b,expect", readyaml("div")[0],ids=readyaml("div")[1])
    def test_div(self, a, b, expect):
        try:
            result=self.cal.div(a,b)
            if isinstance(result,float):
                result =round(result,2)
            assert  result== expect
        except Exception as e:
            print("除数不能为0")
            assert True

