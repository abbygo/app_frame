# abby
import os

import pytest
import yaml

from common.dir_config import data_dir
from page.app import App


class TestProFile:

    def setup_class(self):
        self.main = App().start().main()
        self.profile = self.main.goto_profile()

    def teardown(self):
        self.profile.back()

    def test_go_to_pay_order(self):
        title=self.profile.go_to_pay_order().get_title()
        assert '订单' in title

    def test_go_to_send(self):
        title=self.profile.go_to_send().get_title()
        assert '订单' in title

    def test_go_to_get(self):
        title=self.profile.go_to_get().get_title()
        assert '订单' in title

    def test_go_to_envaluate(self):
        title=self.profile.go_to_envaluate().get_title()
        assert '订单' in title

    def test_get_all_order(self):
        title=self.profile.get_all_order().get_title()
        assert '订单' in title
