# abby
import os

import pytest
import yaml

from common.dir_config import data_dir
from page.app import App


class TestShoppingCart:

    def setup_class(self):
        self.main = App().start().main()
        self.shoping_cart = self.main.goto_shoping_cart()

    def setup(self):
        # 购物车数量是0 ，就切换到分类页面添加商品，
        if self.main.get_shopping_cart_count() == 0:
            self.main.goto_category().switch_category().add_item()
            # 然后在回到购物车页面
            self.main.goto_shoping_cart()

    def test_add_item(self):
        before_count = self.main.get_shopping_cart_count()
        self.shoping_cart.add_item()
        after_count = self.main.get_shopping_cart_count()
        assert before_count + 1 == after_count

    def test_clear_shopping_cart(self):
        self.shoping_cart.clear()
        after_count = self.main.get_shopping_cart_count()
        assert after_count == 0

    def test_remove_item(self):
        before_count = self.main.get_shopping_cart_count()
        self.shoping_cart.remove_item()
        after_count = self.main.get_shopping_cart_count()
        assert before_count - 1 == after_count

    def test_deselect_item(self):
        if not self.shoping_cart.is_all_check():
            self.shoping_cart.all_check()
        before_money = self.shoping_cart.total_price()
        self.shoping_cart.deselect_item()
        after_money = self.shoping_cart.total_price()
        assert after_money <= before_money

    def test_select_item(self):
        if self.shoping_cart.is_all_check():
            self.shoping_cart.all_check()
        before_money = self.shoping_cart.total_price()
        self.shoping_cart.select_item()
        after_money = self.shoping_cart.total_price()
        assert after_money > before_money







