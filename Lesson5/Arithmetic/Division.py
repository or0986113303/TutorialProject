# -*- coding: utf-8 -*-
import sys

# 整數相除
firstinput = 1
secondimput = 2
firstoutput = firstinput / secondimput
print firstoutput

# 浮點數相除
firstinput = 1.0
secondimput = 2.0
firstoutput = firstinput / secondimput
print firstoutput

# 字元相除
try : 
    firstinput = 'Hi'
    secondimput = 2
    firstoutput = firstinput / secondimput 
    print firstoutput
except (RuntimeError, TypeError, NameError):
    print 'Opps !! type error!!'

# 字串相減
try :
    firstinput = 'Hello'
    secondimput = 3
    firstoutput = firstinput / secondimput
    print firstoutput
except (RuntimeError, TypeError, NameError):
    print 'Opps !! type error!!'

# 列表相除
try :
    firstinput = ['Hello','python','!!']
    secondimput = 4
    firstoutput = firstinput / secondimput
    print firstoutput
except (RuntimeError, TypeError, NameError):
    print 'Opps !! type error!!'

# 組合相除
try :
    firstinput = ('Hello','python','!!')
    secondimput = 5
    firstoutput = firstinput / secondimput
    print firstoutput
except (RuntimeError, TypeError, NameError):
    print 'Opps !! type error!!'

# 字典相除
try :
    firstinput = {'1':'Hello','2':'Python','3':'!!'}
    secondimput = 6
    firstoutput = {}
    firstoutput = firstinput / secondimput
    print firstoutput
except (RuntimeError, TypeError, NameError):
    print 'Opps !! type error!!'
    