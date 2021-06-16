#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from app.test_frame.black_handle import black_wrapper


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        # 定义黑名单列表;可以封装一个黑名单类
        self.black_list = [(By.XPATH, '//*[@class=""]')]

    @black_wrapper  # 使用装饰器的方式将find方法扩展
    def find(self, by, locator):
        self.driver.find_element(by, locator)
        # #  处理页面弹框
        # try:
        #     # 如果没找到元素，则去找黑名单元素
        #     self.driver.find_element(by, locator)
        # except Exception as e:
        #     # 遍历黑名单列表
        #     for black in self.black_list:
        #         ele = self.finds(*black)
        #         # 如果页面有黑名单，则去点击关闭
        #         if len(ele) > 0 :
        #             ele[0].click()
        #         # 处理完黑名单后再去查找页面元素
        #         return self.find(by, locator)
        #     # 如果没有页面元素，也没有黑名单，则抛出异常
        #     raise e

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_and_click(self, by, locator):
        return self.driver.find_element(by, locator).click()

    def find_and_scroll(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
            .scrollable(true).instance(0))\
            .scrollIntoView(new UiSelector()\
            .text("{text}").instance(0));')
