# yaml动作详解

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

```

| 动作（action）    | 解释                                             |
| ----------------- | ------------------------------------------------ |
| click             | 执行点击操作                                     |
| text              | 获取文本                                         |
| click_by_index    | 点击通过索引，适合通过表达式可以获取多个元素     |
| send              | 发送文本                                         |
| len > 0           | 判断元素的长度是否大于0，大于0返回True,否则False |
| get_text_by_index | 通过索引获取文本，适合通过表达式可以获取多个元素 |
