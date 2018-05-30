# -*- coding: utf-8 -*-
import sys

# 整數相減
firstinput = 1
secondimput = 2
firstoutput = firstinput - secondimput
print firstoutput

# 浮點數相減
firstinput = 1.0
secondimput = 2.0
firstoutput = firstinput - secondimput
print firstoutput

# 字元相減
firstinput = 'H'
secondimput = 'i'
firstoutput = chr(abs(ord(firstinput) - ord(secondimput)))
print firstoutput

# 字串相減
try :
    firstinput = 'Hello '
    secondimput = 'python'
    firstoutput = firstinput - secondimput
    print firstoutput
except (RuntimeError, TypeError, NameError):
    print 'Opps !! type error!!'

# 列表相加
try :
    firstinput = ['Hello','python','!!']
    secondimput = ['This','is','Mir',',','Chen']
    firstoutput = firstinput - secondimput
    print firstoutput
except (RuntimeError, TypeError, NameError):
    print 'Opps !! type error!!'

# 組合相減
try :
    firstinput = ('Hello','python','!!')
    secondimput = ('This','is','Mir',',','Chen')
    firstoutput = firstinput - secondimput
    print firstoutput
except (RuntimeError, TypeError, NameError):
    print 'Opps !! type error!!'

# 字典相減
try :
    firstinput = {'1':'Hello','2':'Python','3':'!!'}
    secondimput = {'4':'Thie','5':'is','6':'Mir','7':',','8':'chen'}
    firstoutput = {}
    firstoutput = firstinput - secondimput
    print firstoutput
except (RuntimeError, TypeError, NameError):
    print 'Opps !! type error!!'
    