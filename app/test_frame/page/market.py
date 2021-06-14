#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from app.test_frame.base_page import BasePage
from app.test_frame.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.find_and_click(By.XPATH, '')
        return Search(self.driver)
