import os

from common.base_page import BasePage
from common.dir_config import yaml_path


class Profile(BasePage):
    path = os.path.join(yaml_path, "profile.yaml")

    def go_to_pay_order(self):
        self.steps(self.path)
        return self

    def go_to_send(self):
        self.steps(self.path)
        return self

    def go_to_get(self):
        self.steps(self.path)
        return self

    def go_to_envaluate(self):
        self.steps(self.path)
        return self

    def get_all_order(self):
        self.steps(self.path)
        return self
