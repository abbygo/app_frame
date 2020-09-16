#abby
import os

from common.base_page import BasePage
from common.dir_config import  yaml_path
from page.category_page import CategoryPage
from page.commodity_details_page import CommodityDetailsPage
from page.shoping_cart_page import ShopingCartPage


class FirstPage(BasePage):
    path = os.path.join(yaml_path, 'first.yaml')
    def get_first_item_name(self):
        '''
            进入到商品详情
            '''
        res=self.steps(self.path)
        return res

    def goto_commodity_details(self):
        '''
            进入到商品详情
            '''
        self.steps(self.path)
        return CommodityDetailsPage(self._driver)
    def goto_category(self):
        '''
            进入商品分类
            '''
        self.steps(self.path)
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
        self.steps(self.path)
        return self
    def add_item_to_shop_cart(self):
        '''
           添加商品进入购物车
           '''
        res=self.steps(self.path)
        return res

    def choose_specifications_add_item_to_shop_cart(self):
        '''
           # 选择规格后加入购物车，比如肉就要250k,500k
           '''
        self.steps(self.path)
        return ShopingCartPage(self._driver)





