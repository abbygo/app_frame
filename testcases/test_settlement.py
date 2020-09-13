# abby
import os

import pytest
import yaml

from common.dir_config import data_dir
from page.app import App


class TestSettlement:

    def setup_class(self):
        self.main = App().start().main()

    def setup(self):
        # 购物车数量是0 ，就切换到分类页面添加商品，
        if self.main.get_shopping_cart_count() == 0:
            self.main.goto_category().switch_category().add_item()
            # 然后在回到购物车页面
            self.main.goto_shoping_cart()

    @pytest.mark.parametrize('data',
                             yaml.safe_load(open(os.path.join(data_dir, 'data_settlement.yaml'), encoding='utf-8')))
    def test_shopping_cart_to_settlement(self, data):
        self.settlement_page=self.main.goto_shoping_cart().goto_settlement_page()
        if self.settlement_page.is_addr():
            self.settlement_page.add_pick_up_point(data['name'],data['phone'])
        if self.settlement_page.slide_to_bottom().is_open_item_but():
            self.settlement_page.open_item_list()
        self.settlement_page.slide_to_bottom().goto_pay_page()

    def test_commodity_details_page_to_settlement(self):
        self.main.goto_home().slide_to_bottom().goto_commodity_details().goto_settlement_page()


