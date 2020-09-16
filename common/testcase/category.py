
import os

from common.base_page import BasePage
from common.dir_config import yaml_path


class Category(BasePage):
    path = os.path.join(yaml_path, "category.yaml")

    def search_item(self):
        self.steps(self.path)
        return self
   
    def switch_category(self):
        self.steps(self.path)
        return self
   
    def add_item(self):
        self.steps(self.path)
        return self
   
    def is_goto_category(self):
        self.steps(self.path)
        return self
   