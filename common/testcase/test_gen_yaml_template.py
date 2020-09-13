# abby
from common.ext.make import gen_py_template, read_py_file






def test_read_py_file():
    res=read_py_file(r'C:\Users\lnz\PycharmProjects\app_xinfuyoucai_frame\page\yaml\commodity_details.yaml')

    gen_py_template(*res)
