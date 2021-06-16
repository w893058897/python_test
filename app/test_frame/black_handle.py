#!/usr/bin/env python
# -*- coding: utf-8 -*-

def black_wrapper(fun):
    def run(*args, **kwargs):
        basepage = args[0]  # 取fun函数中的第一个参数也就是self,第二个参数是by
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            # 遍历黑名单列表
            for black in basepage.black_list:
                ele = basepage.finds(*black)
                # 如果页面有黑名单，则去点击关闭
                if len(ele) > 0:
                    ele[0].click()
                # 处理完黑名单后再去查找页面元素
                return fun(*args, **kwargs)
            # 如果没有页面元素，也没有黑名单，则抛出异常
            raise e

    return run
