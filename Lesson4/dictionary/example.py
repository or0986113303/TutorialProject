# -*- coding: utf-8 -*-
import sys

# 一個空的組合
aemptydictionary = {}

# 列印出一個組合
print aemptydictionary

# 我想給組合一點東西
dictionaryatfirst = {'lastname':'chen','firstname':'mir'}
print dictionaryatfirst
print dictionaryatfirst['lastname']
print dictionaryatfirst['firstname']

# 可以事後再加入嗎
dictionaryatfirst.update({'test': 3})
print dictionaryatfirst['test']
dictionaryatfirst['simple'] = 4
print dictionaryatfirst['simple']
print dictionaryatfirst

print dictionaryatfirst.keys()
print dictionaryatfirst.values()

