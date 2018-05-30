# -*- coding: utf-8 -*-
import sys

# 列印出系統認知的一個整數要多少儲存空間
print sys.getsizeof(sys.maxint + 1)

# 試試看長整數能有多長
longnumberlengthtest = 35184372088831L
print longnumberlengthtest
print sys.getsizeof(longnumberlengthtest)

# 再多一點會怎麼樣呢 ?
print longnumberlengthtest + 1
print sys.getsizeof(longnumberlengthtest + 1)
