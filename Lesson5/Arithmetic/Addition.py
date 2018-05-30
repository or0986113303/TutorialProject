# -*- coding: utf-8 -*-
import sys

# 整數相加
firstinput = 1
secondimput = 2
firstoutput = firstinput + secondimput
print firstoutput

# 浮點數相加
firstinput = 1.0
secondimput = 2.0
firstoutput = firstinput + secondimput
print firstoutput

# 字元相加
firstinput = 'H'
secondimput = 'i'
firstoutput = firstinput + secondimput
print firstoutput

# 字串相加
firstinput = 'Hello '
secondimput = 'python'
firstoutput = firstinput + secondimput
print firstoutput

# 列表相加
firstinput = ['Hello','python','!!']
secondimput = ['This','is','Mir',',','Chen']
firstoutput = firstinput + secondimput
print firstoutput

# 組合相加
firstinput = ('Hello','python','!!')
secondimput = ('This','is','Mir',',','Chen')
firstoutput = firstinput + secondimput
print firstoutput

# 字典相加
firstinput = {'1':'Hello','2':'Python','3':'!!'}
secondimput = {'4':'Thie','5':'is','6':'Mir','7':',','8':'chen'}
firstoutput = {}
firstoutput.update(firstinput)
firstoutput.update(secondimput)
print firstoutput

# 字典內容相加
firstinput = {'1':'Hello','2':'Python','3':'!!'}
secondimput = {'1':'Thie','2':'is','3':'Mir','4':',','5':'chen'}
firstoutput = {}
firstoutput = firstinput + secondimput