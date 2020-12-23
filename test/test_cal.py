import pytest
import yaml

from pythoncode.calculator import Calculator


def readyaml(name: str):
    with open("./data.yaml") as f:
        dict1 = yaml.safe_load(f)
    print(dict1)
    list1 = dict1[name]
    return list1

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

    @pytest.mark.parametrize("a,b,expect",readyaml("add"))
    def test_add(self,a,b,expect):
        assert self.cal.add(a,b)==expect

    @pytest.mark.parametrize("a,b,expect",readyaml("sub"))
    def test_sub(self,a,b,expect):
        assert self.cal.sub(a,b)==expect

    @pytest.mark.parametrize("a,b,expect", readyaml("mul"))
    def test_mul(self, a, b, expect):
        assert self.cal.mul(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", readyaml("div"))
    def test_div(self, a, b, expect):
        if b==0:
            with pytest.raises(ValueError) as f:
                self.cal.div(a,b)
            assert f.value.args[0]=="除数不能为0"
            assert f.type==ValueError
        else:
            assert self.cal.div(a,b) == expect

