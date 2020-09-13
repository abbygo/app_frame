# abby
import os

from common.base_page import BasePage
from common.dir_config import page_path
from page.settlement_page import SettlementPage


class ShopingCartPage(BasePage):

    def goto_settlement_page(self):
        '''
        去结算页面
        :return:
        '''
        # 点击结算按钮
        self.steps(os.path.join(page_path, 'shopping_cart.yaml'))
        return SettlementPage(self._driver)

    def clear(self):
        # 清空购物车
        self.steps(os.path.join(page_path, 'shopping_cart.yaml'))
        return self

    def add_item(self):
        # 添加商品
        self.steps(os.path.join(page_path, 'shopping_cart.yaml'))
        return self

    def remove_item(self):
        # 删除商品
        self.steps(os.path.join(page_path, 'shopping_cart.yaml'))
        return self

    def deselect_item(self):
        # 取消选中的商品
        self.steps(os.path.join(page_path, 'shopping_cart.yaml'))
        return self

    def select_item(self):
        # 选中商品
        self.steps(os.path.join(page_path, 'shopping_cart.yaml'))
        return self

    # 合计金额
    def total_price(self):
        price = self.steps(os.path.join(page_path, 'shopping_cart.yaml'))
        # 返回的数据是合计: ¥52.50  ，---》切割后得到52.50
        price = price.split("¥")[-1]
        return price

    # 检查是否全选全选按钮
    def is_all_check(self):
        res = self.steps(os.path.join(page_path, 'shopping_cart.yaml'))
        return res

    # 全选
    def all_check(self):
        self.steps(os.path.join(page_path, 'shopping_cart.yaml'))
        return self
