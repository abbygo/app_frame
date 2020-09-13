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
