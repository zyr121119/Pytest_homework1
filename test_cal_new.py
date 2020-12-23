import yaml
from pytest import approx
import pytest


class TestCal():
    @pytest.mark.run(order=1)
    def test_add(self,get_cal,get_adddata):
        try:
            cal = get_cal
            list1 = get_adddata
            assert cal.add(list1[0], list1[1]) == approx(list1[2], rel=1e-2)
        except Exception as e:
                print("参数异常")
                assert False

    @pytest.mark.run(order=4)
    def test_div(self, get_cal,get_divdata):
        try:
            cal = get_cal
            list1 = get_divdata
            print("test_div")
            assert cal.div(list1[0], list1[1]) == approx(list1[2], 1e-2)
        except Exception as e:
            if e==ZeroDivisionError:
                print("除数不能为0")
                assert True

    @pytest.mark.run(order=2)
    def test_sub(self, get_cal, get_subdata):
        try:
            cal = get_cal
            list1 = get_subdata
            assert cal.sub(list1[0], list1[1]) == approx(list1[2], 1e-2)
        except Exception as e:
            print("参数异常")
            assert False

    @pytest.mark.run(order=3)
    def test_mul(self, get_cal, get_muldata):
        try:
            cal = get_cal
            list1 = get_muldata
            assert cal.mul(list1[0], list1[1]) == approx(list1[2], 1e-2)
        except Exception as e:
            print("参数异常")
            assert False






