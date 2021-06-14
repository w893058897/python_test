#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from app.test_frame.base_page import BasePage


class Search(BasePage):
    def search(self):
        self.find(By.XPATH, '').send_keys()
        return True
