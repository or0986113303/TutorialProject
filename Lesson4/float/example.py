# -*- coding: utf-8 -*-
import sys

# 列印出系統認知的一個浮點數是甚麼
print sys.float_info

# 試試看長整數能有多長
floatumberlengthtest = 1.7976931348623157e+308
print floatumberlengthtest
print sys.getsizeof(floatumberlengthtest)

# 再多一點會怎麼樣呢 ?
print floatumberlengthtest * 2
print sys.getsizeof(floatumberlengthtest * 2)
