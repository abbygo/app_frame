# abby
import os

import pytest
import yaml

from common.dir_config import data_dir
from page.app import App


class TestProFile:

    def setup_class(self):
        self.main=App().start().main()
        self.profile = self.main.goto_profile()

    def test_go_to_pay_order(self):

        self.profile.go_to_pay_order()

    def test_go_to_send(self):
        self.profile.go_to_send()

    def test_go_to_get(self):
        self.profile.go_to_get()

    def test_go_to_envaluate(self):
        self.profile.go_to_envaluate()
    def test_get_all_order(self):
        self.profile.get_all_order()






