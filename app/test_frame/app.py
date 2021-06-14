#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver

from app.test_frame.base_page import BasePage
from app.test_frame.page.mainpage import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = {}
            caps['platformName'] = 'Android'
            caps['deviceName'] = '127.0.0.1:7555'
            caps['appPackage'] = 'com.xueqiu.android'
            caps['appActivity'] = 'com.huawei.hms.activity.BridgeActivity'
            caps['noReset'] = True
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)
        return self

    def restart(self):
        # 重启app
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        # 停止app
        self.driver.quit()

    def goto_main(self) -> MainPage:
        # 进入app首页
        return MainPage(self.driver)
