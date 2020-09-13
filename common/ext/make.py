import subprocess
import sys
from pathlib import Path
from typing import Text, NoReturn

import jinja2
import yaml
from loguru import logger
from sentry_sdk import capture_exception

from common.utils import is_support_multiprocessing


def format_pytest_with_black(*python_paths: Text) -> NoReturn:
    logger.info("format pytest cases with black ...")
    try:
        if is_support_multiprocessing() or len(python_paths) <= 1:
            subprocess.run(["black", *python_paths])
        else:
            logger.warning(
                f"this system does not support multiprocessing well, format files one by one ..."
            )
            [subprocess.run(["black", path]) for path in python_paths]
    except subprocess.CalledProcessError as ex:
        capture_exception(ex)
        logger.error(ex)
        sys.exit(1)
    except FileNotFoundError:
        err_msg = """
missing dependency tool: black
install black manually and try again:
$ pip install black
"""
        logger.error(err_msg)
        sys.exit(1)


def print_gen_py_page_log_and_formart(file_type: Text):
    '''
    生成日志和格式化文件
    :param file_type:
    :return:
    '''

    def dec(fun):
        def wrapper(*args, **kwargs):
            logger.info(f"dump yaml to {file_type} format.")
            file_name = fun(*args, **kwargs)
            logger.info(f"Generate {file_type} page successfully: {file_name}")
            # 只格式化py文件
            if str(file_name).endswith('py'):
                format_pytest_with_black(file_name)
            return file_name

        return wrapper

    return dec


def read_py_file(file_name):
    # {'search_item': [{'by': 'id', 'locator': 'com.xfyoucai.youcai:id/searchLayout', 'action': 'click'},
    p = Path(file_name)
    out_file_name = str(p.stem) + ".py"
    yaml_file_name = str(p.stem) + ".yaml"
    class_name = str(p.stem).capitalize()
    with open(file_name, encoding='utf-8') as f:
        content_dict = yaml.safe_load(f)
        method_name_list = list(content_dict.keys())

    return out_file_name, class_name, method_name_list, yaml_file_name


@print_gen_py_page_log_and_formart('py')
def gen_py_template(file_name: Text, class_name: Text, method_name_list, yaml_file_name):
    '''
    生成yaml文件

    '''
    # 方法名，文件名
    __TEMPLATE__ = jinja2.Template(
        """
import os

from common.base_page import BasePage
from common.dir_config import yaml_path


class {{class_name}}(BasePage):
    path = os.path.join(yaml_path, "{{yaml_file_name}}")
{% for method_name in method_name_list %}
    def {{method_name}}(self):
        self.steps(self.path)
        return self
   {% endfor %}
"""
    )

    data = {
        "class_name": class_name,
        "yaml_file_name": yaml_file_name,
        "method_name_list": method_name_list

    }
    # 渲染模板
    content = __TEMPLATE__.render(data)
    # 新产生py文件
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)

    return file_name
