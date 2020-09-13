# abby
import os

import pytest
import yaml

from common.dir_config import data_dir
from page.app import App


class TestCategory:

    def setup_class(self):
        self.main=App().start().main()
        self.category = self.main.goto_category()

    def test_add_item(self):
        #添加商品
        add_before_shopping_count=self.main.get_shopping_cart_count()
        self.category.add_item()
        add_after_shopping_count = self.main.get_shopping_cart_count()

        assert  add_after_shopping_count > add_before_shopping_count

    def test_switch_category(self):
        #切换商品分类后添加商品
        add_before_shopping_count=self.main.get_shopping_cart_count()
        self.category.switch_category().add_item()
        add_after_shopping_count = self.main.get_shopping_cart_count()
        assert  add_after_shopping_count > add_before_shopping_count

    def test_search_item(self):
        #搜索后添加商品
        add_before_shopping_count=self.main.get_shopping_cart_count()
        self.category.search_item()
        add_after_shopping_count = self.main.get_shopping_cart_count()
        assert  add_after_shopping_count > add_before_shopping_count


