#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from app.test_frame.base_page import BasePage
from app.test_frame.page.market import Market


class MainPage(BasePage):
    def goto_market(self):
        self.find_and_click(By.XPATH, '')
        return Market(self.driver)
