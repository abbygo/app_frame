#abby
import os

from common.base_page import BasePage
from common.dir_config import page_path
from page.category_page import CategoryPage
from page.commodity_details_page import CommodityDetailsPage
from page.shoping_cart_page import ShopingCartPage


class FirstPage(BasePage):
    def get_first_item_name(self):
        '''
            进入到商品详情
            '''
        res=self.steps(os.path.join(page_path, 'first.yaml'))
        return res

    def goto_commodity_details(self):
        '''
            进入到商品详情
            '''
        self.steps(os.path.join(page_path, 'first.yaml'))
        return CommodityDetailsPage(self._driver)
    def goto_category(self):
        '''
            进入商品分类
            '''
        self.steps(os.path.join(page_path, 'first.yaml'))
        return CategoryPage(self._driver)

    def goto_member_recharge(self):
        '''
           进入到会员充值页面
           '''
        pass


    def slide_to_bottom(self):
        '''
            进入商品分类
            '''
        self.steps(os.path.join(page_path, 'first.yaml'))
        return self
    def add_item_to_shop_cart(self):
        '''
           添加商品进入购物车
           '''
        self.steps(os.path.join(page_path, 'first.yaml'))
        return ShopingCartPage(self._driver)



