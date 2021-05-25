#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDemo:

    def setup(self):
        # 浏览器复用
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # 没添加cookies的时候打开需要扫码登录
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        time.sleep(2)
        # 添加cookies后，可以跳过登录
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
             'value': ''},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850806047318'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'nhC5p7_6G7rbCpDSIAb1u2Aso--cNsc-pb_KBkEAHyTCv_xo1EOuxiHBTRPl2bJf8_KglcKE3HMeVtBD8JhTJFtcC9Ff45NwsvHPUGt0KcleN2XzUmh7fmlkc4a-5LUHNNbSyIECm6mwe94FLja1Zqewz2HjCiTL44AeKwuAOdMglf97_rnjagB87vKOIPzuQz4UKGwfZQIgyAz2fWsoJdrHrPRiLlUmwg81Ju9yPiFoTxvEdW04nt6e-znGKybcZ3Gh3S1CK6ZFVHGm9oPUgw'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850806047318'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324975459596'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1649662050, 'httpOnly': False,
                                  'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                                  'value': '1618122561'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a6336919'},
            {'domain': '.qq.com', 'expiry': 1622043591, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1241064796.1621957165'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1621988688, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '8l60ji7'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '01740540'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1624549192, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': '9DulUB4OwdefekNlBl6yRskcisQNRWgU7_JlkjZZ-mLdHavsPE7SYKy3JJ4u12Tg'},
            {'domain': '.qq.com', 'expiry': 1685029191.1234, 'httpOnly': False, 'name': '_ga', 'path': '/',
             'secure': False, 'value': 'GA1.2.1257192987.1618122563'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1649658557, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'}]
        # 当expiry时间戳中有浮点数时，会报错，可以直接删除该key和value
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        time.sleep(2)
