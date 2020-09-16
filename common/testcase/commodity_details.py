
import os

from common.base_page import BasePage
from common.dir_config import yaml_path


class Commodity_details(BasePage):
    path = os.path.join(yaml_path, "commodity_details.yaml")

    def add_item(self):
        self.steps(self.path)
        return self
   
    def get_item_name(self):
        self.steps(self.path)
        return self
   
    def goto_settlement_page(self):
        self.steps(self.path)
        return self
   
    def get_item_price(self):
        self.steps(self.path)
        return self
   
    def get_item_number(self):
        self.steps(self.path)
        return self
   