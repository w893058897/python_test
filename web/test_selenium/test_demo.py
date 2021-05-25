#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDemo:

    def setup(self):
        # 浏览器复用
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        # self.driver.get('https://ceshiren.com')
        self.driver.find_element_by_xpath('//li[@title="所有分类"]').click()
        categoryele = self.driver.find_element_by_xpath('//li[@title="所有分类"]')
        assert 'active ember-view' == categoryele.get_attribute("class")
