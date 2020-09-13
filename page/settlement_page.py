import os

from common.base_page import BasePage
from common.dir_config import  yaml_path


class SettlementPage(BasePage):
    '''
    结算页面(确定订单页面)
    '''
    path = os.path.join(yaml_path, 'settlement.yaml')
    def is_addr(self):
        # 检查是否有添加地址
        res=self.steps(self.path)
        return res
    #添加收货地址
    def add_pick_up_point(self,name,phone):
        self._params['name'] = name
        self._params['phone'] = phone
        self.steps(self.path)
        return self


    #选择收货地址
    def select_pick_up_point(self):
        self.steps(self.path)
        return self

    # 检查是否有展示商品详情按钮
    def is_open_item_but(self):
        res=self.steps(self.path)
        return res

    def open_item_list(self):
        # 展开商品详情
        self.steps(self.path)
        return self

    def slide_to_bottom(self):
        self.steps(self.path)
        return self

    def view_balance(self):
        # 查看余额
        self.steps(self.path)

        return self

    def goto_pay_page(self):
        # 进入到支付页面
        self.steps(self.path)
        return self
