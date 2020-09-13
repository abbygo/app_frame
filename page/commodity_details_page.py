# abby
import os

from common.base_page import BasePage
from common.dir_config import  yaml_path
from page.settlement_page import SettlementPage


class CommodityDetailsPage(BasePage):
    '''
    商品详情页面
    '''
    path = os.path.join(yaml_path, 'commodity_details.yaml')
    def add_item(self):
        '''
        点击加入购物车按钮
        :return:
        '''
        self.steps(self.path)
        return self

    def goto_settlement_page(self):
        '''
        点击立即购买按钮,选择规则、数量，点确定，进入到结算页面
        :return:
        '''
        self.steps(self.path)
        return SettlementPage(self._driver)
    def get_item_name(self):
        '''
           获取商品名称
           '''
        res = self.steps(self.path)
        return res
    def get_item_price(self):
        '''
           获取商品价格
           '''
        res = self.steps(self.path)
        #¥9.9--->9.9
        res=res.split('¥')[-1]
        return float(res)

    def get_item_number(self):
        '''
           获取购买数量
           '''
        res = self.steps(self.path)
        return int(res)



