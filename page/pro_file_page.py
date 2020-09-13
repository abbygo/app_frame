#abby
import os

from common.base_page import BasePage
from common.dir_config import page_path


class ProFilePage(BasePage):
    def go_to_pay_order(self):
        self.steps(os.path.join(page_path, 'profile.yaml'))
        return self

    def go_to_send(self):
        self.steps(os.path.join(page_path, 'profile.yaml'))
        return self

    def go_to_get(self):
        self.steps(os.path.join(page_path, 'profile.yaml'))
        return self

    def go_to_envaluate(self):
        self.steps(os.path.join(page_path, 'profile.yaml'))
        return self



    def get_all_order(self):
        self.steps(os.path.join(page_path, 'profile.yaml'))
        return self


