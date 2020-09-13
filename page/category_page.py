# abby
import os

from common.base_page import BasePage
from common.dir_config import yaml_path


class CategoryPage(BasePage):
    '''
    分类
    '''
    path = os.path.join(yaml_path, 'category.yaml')

    def search_item(self):
        '''
        搜索商品
        :return:
        '''
        # 输出搜索内容--》选中输出的搜索内容--》
        self.steps(self.path)
        return self

    def switch_category(self):
        '''
        切换分类
        :return:
        '''
        self.steps(self.path)
        return self

    def add_item(self):
        self.steps(self.path)
        return self

    def is_goto_category(self):
        '''
           是否到达分类页面
           '''
        res = self.steps(self.path)
        return res
