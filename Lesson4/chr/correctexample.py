# -*- coding: utf-8 -*-
import io
import sys

# 列印出英文 I
print 'I'

# 列印出英文 I 的長度
print len('I')

# 列印出中文 我
print u'我'.encode('cp950')

# 列印出中文 我 的長度
print len(u'我'.encode('cp950'))

# 確認系統預設的編碼
print sys.getdefaultencoding()
