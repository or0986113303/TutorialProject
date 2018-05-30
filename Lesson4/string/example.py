# -*- coding: utf-8 -*-
import io
import sys

# 列印出英文 I
englishstring = 'I\'mir Chen'
print englishstring[:]
print englishstring[0]

# 列印出中文 我
chinesestring = u'我是陳米爾'.encode('cp950')
print chinesestring[:]
print chinesestring[0:2]

# 確認系統預設的編碼
print sys.getdefaultencoding()
