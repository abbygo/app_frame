# app_frame介绍

app_frame 是一个UI测试框架

## 设计理念

约定超过配置

整合了appium 、pytest 、allure

## 主要特点

- 集成了appium 的强大功能

- 融合了PO设计模式

- 可以根据YAML数据格式自动生成page页面，提升工作效率

- 使用[`pytest，`](https://docs.pytest.org/数百个插件随时可用。

- 有了[`诱惑力`](https://docs.qameta.io/allure/)，测试报告可以相当不错和强大

  

# 如何开始？ 



## yaml动作详解

```
demo.yaml
#方法名
add_item:
#定位方式
 - by: id
 #定位表达式
   locator: "com.xfyoucai.youcai:id/tv_add_shop_car"
 #动作：点击
   action: click
get_item_price:
 - by: id
   locator: "com.xfyoucai.youcai:id/tv_sku_price"
   action: text
goto_settlement_page:
 - by: id
   locator: "com.xfyoucai.youcai:id/tv_text"
   action: click_by_index
add_pick_up_point:
 - by: id
   locator: "com.xfyoucai.youcai:id/mPickupNameEtn"
   action: send
   value: ${name}
#检查是否有添加地址
is_addr:
 - by: id
   locator: "com.xfyoucai.youcai:id/tv_no_addr"
   action: len > 0
open_item_list:
 - by: id
   locator: "com.xfyoucai.youcai:id/downArrowImg"
   action: get_text_by_index
slide_to_bottom:
#滑动到具体的文本按钮上
 - text: "余额明细"
   action: scroll

```

| 动作（action）    | 解释                                             |
| ----------------- | ------------------------------------------------ |
| click             | 执行点击操作                                     |
| text              | 获取文本                                         |
| click_by_index    | 点击通过索引，适合通过表达式可以获取多个元素     |
| send              | 发送文本                                         |
| len > 0           | 判断元素的长度是否大于0，大于0返回True,否则False |
| get_text_by_index | 通过索引获取文本，适合通过表达式可以获取多个元素 |
| scroll            | 滚动到指定文本的地方                             |

# 变量替换

yaml文件中：${变量名},表示需要替换变量

```
 - by: id
   locator: "com.xfyoucai.youcai:id/mPickupNameEtn"
   action: send
   value: ${name}
```

page.py 传递需要替换的值，key 需要与yaml文件中的key保持一致

```
  #添加收货地址
    def add_pick_up_point(self,name):
        self._params['name'] = name
        self.steps(self.path)
        return self
```

# 生成xx_page.py文件



```
准备工作

#安装pyinstaller
pip install pyinstaller
#进入到C:\Users\lnz\PycharmProjects\app_xinfuyoucai_frame\common\ext\lient.py目录下，执行生成exe单文件的命名，-n 是指定exe应用的名称
pyinstaller -F client.py -n ext2page
#在client.py文件的目录下，产生dist文件夹，文件夹里有一个ext2page.exe;复制ext2page.exe到虚拟环境下;eg：D:\tutorial-env\Scripts；
#删除刚才产生的多余文件后，执行如下命令


运行：ext2page -h ，验证是否安装成功
(tutorial-env) C:\Users\lnz\PycharmProjects\app_xinfuyoucai_frame\common\ext>ext2page -h
usage: ext2page [-h] -Y [YAML_SOURCE_FILE]

optional arguments:
  -h, --help            show this help message and exit
  -Y [YAML_SOURCE_FILE], --yaml_source_file [YAML_SOURCE_FILE]
                        Specify YAML source file





```

```
生成page文件
(tutorial-env) C:\Users\lnz\PycharmProjects\app_xinfuyoucai_frame\common\ext>ext2page -Y C:\Users\lnz\PycharmProjects\app_x
infuyoucai_frame\page\yaml\profile.yaml
2020-09-13 19:37:37.195 | INFO     | common.ext.make:wrapper:48 - dump yaml to py format.
2020-09-13 19:37:37.207 | INFO     | common.ext.make:wrapper:50 - Generate py page successfully: profile.py
2020-09-13 19:37:37.209 | INFO     | common.ext.make:format_pytest_with_black:16 - format pytest cases with black ...
reformatted profile.py
All done! ✨ � ✨
1 file reformatted.
```

