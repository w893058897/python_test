#!/usr/bin/env python
# -*- coding: utf-8 -*-
from money import saved_money
import send_money


def select_money():
    sum_money = send_money.money + saved_money
    print(f"发工资后的总存款为：{sum_money}")
