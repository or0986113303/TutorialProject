# -*- coding: utf-8 -*-
import sys

# 一個空的組合
aemptytuple = ()

# 列印出一個組合
print aemptytuple

# 我想給組合一點東西
tuplewithnumbersatfirst = (1,2,3,4,5,6,7,8,9,10)
print tuplewithnumbersatfirst

# 組合只能與組合相加或相乘
tuplewithnumbersatferfirst = tuplewithnumbersatfirst
tuplewithnumbersatferfirst += tuplewithnumbersatfirst
print tuplewithnumbersatferfirst
tuplewithnumbersatferfirst *= 2
print tuplewithnumbersatferfirst


