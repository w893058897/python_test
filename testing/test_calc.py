#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml

import pytest

from python_code.calc import Calculator

with open('./datas/calc.yaml') as f:
    data = yaml.safe_load(f)
    add_data = data['add']['datas']
    myid = data['add']['myid']
    sub_data = data['sub']['datas']
    sub_myid = data['sub']['myid']

class TestCalc:

    def setup_class(self):
        print("开始计算。。。")
        # 实例化计算器类
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize(
        "a, b, expect", add_data, ids=myid  # 指定测试用例名称
    )
    def test_add(self, a, b, expect):
        # 实例化计算器类
        # calc = Calculator()
        # 调用加法方法
        result = self.calc.sum(a, b)
        # 判断结果类型是否为浮点型
        if isinstance(result, float):
            result = round(result, 2)
        # 进行断言
        assert result == expect

    @pytest.mark.parametrize('a, b, expect', sub_data, ids=sub_myid)
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    # def test_add1(self):
    #     # 实例化计算器类
    #     # calc = Calculator()
    #     # 调用加法方法
    #     result = self.calc.sum(0.1, 0.1)
    #     # 进行断言
    #     assert result == 0.2
    #
    # def test_add2(self):
    #     # 实例化计算器类
    #     # calc = Calculator()
    #     # 调用加法方法
    #     result = self.calc.sum(-1, -1)
    #     # 进行断言
    #     assert result == -2
    # def test_add3(self):
    #     result = self.calc.sum(0.1, 0.2)
    #     # round方法，保留两位小数
    #     assert round(result, 2) == 0.3
