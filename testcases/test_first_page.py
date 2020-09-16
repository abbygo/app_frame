# abby
import os

import pytest
import yaml

from common.dir_config import data_dir
from page.app import App


class TestFirstPage:

    def setup_class(self):
        self.main=App().start().main()
        self.home = self.main.goto_home()

    def test_goto_category(self):
        res = self.home.goto_category().is_goto_category()
        self.main.goto_home()
        assert res == True

    def test_add_item_to_shop_cart(self):
        before_count=self.main.get_shopping_cart_count()
        res=self.home.slide_to_bottom().add_item_to_shop_cart()
        if res:
            self.home.choose_specifications_add_item_to_shop_cart()
        after_count=self.main.get_shopping_cart_count()
        assert before_count+1==after_count




    def test_goto_commodity_details(self):
        before_name=self.home.slide_to_bottom().get_first_item_name()
        after_name=self.home.goto_commodity_details().get_item_name()
        assert after_name in before_name







