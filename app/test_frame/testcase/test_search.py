#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.test_frame.app import App


class TestSearch:
    def setup(self):
        self.app = App()

    def test_search(self):
        self.app.start().goto_main().goto_market().goto_search().search()
