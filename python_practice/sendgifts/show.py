#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from gift import have_gift
import gift


def show():
    have_gift = gift.have_gift
    if have_gift == True:
        print("收到礼物啦")
    else:
        print("没有收到礼物")
