# abby
import os


from common.base_page import BasePage
from common.dir_config import page_path


class CategoryPage(BasePage):
    '''
    分类
    '''

    def search_item(self):
        '''
        搜索商品
        :return:
        '''
        # 输出搜索内容--》选中输出的搜索内容--》
        self.steps(os.path.join(page_path, 'category.yaml'))
        return self

    def switch_category(self):
        '''
        切换分类
        :return:
        '''
        self.steps(os.path.join(page_path, 'category.yaml'))
        return self

    def add_item(self):
        self.steps(os.path.join(page_path, 'category.yaml'))
        return self

    def is_goto_category(self):
        '''
           是否到达分类页面
           '''
        res=self.steps(os.path.join(page_path, 'category.yaml'))
        return res




