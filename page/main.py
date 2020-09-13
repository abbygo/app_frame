#abby
import os

from selenium.common.exceptions import NoSuchElementException

from common.base_page import BasePage
from common.dir_config import page_path
from page.category_page import CategoryPage
from page.first_page import FirstPage
from page.pro_file_page import ProFilePage
from page.shoping_cart_page import ShopingCartPage




class Main(BasePage):
    '''
    进入首页
    '''
    def goto_home(self):
        self.steps(os.path.join(page_path,'main.yaml'))
        return FirstPage(self._driver)
    '''
    进入分类
    '''
    def goto_category(self):
        self.steps(os.path.join(page_path,'main.yaml'))
        return CategoryPage(self._driver)


    '''
    进入购物车
    '''
    def goto_shoping_cart(self):
        self.steps(os.path.join(page_path,'main.yaml'))
        return ShopingCartPage(self._driver)

    '''
    进入我的
    '''
    def goto_profile(self):
        self.steps(os.path.join(page_path,'main.yaml'))
        return ProFilePage(self._driver)

    def get_shopping_cart_count(self):
        # 获取购物车数量
        try:
            count = self.steps(os.path.join(page_path, 'main.yaml'))
        # 购物车数量是0 的时候需要处理一下
        except NoSuchElementException:
            return 0
        return int(count)