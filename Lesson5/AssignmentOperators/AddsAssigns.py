# -*- coding: utf-8 -*-
import sys

# 整數賦予
firstinput = 1
firstoutput = 0
firstoutput += firstinput
print firstoutput

print '============================='

# 浮點數相等
firstinput = 1.0
firstoutput = 0.0
firstoutput += firstinput
print firstoutput

print '============================='

# 字元相等
firstinput = 'I'
firstoutput = ''
firstoutput += firstinput
print firstoutput

print '============================='

# 字串相等
firstinput = 'Hello Python!'
firstoutput = ''
firstoutput += firstinput
print firstoutput

print '============================='

# 列表相等
firstinput = ['Hello','Python','!!']
firstoutput = []
firstoutput += firstinput 
print firstoutput

print '============================='

# 組合相等
firstinput = ('Hello','Python','!!')
firstoutput = ()
firstoutput += firstinput
print firstoutput

print '============================='

# 字典相等
firstinput = {'1':'Hello','2':'Python','3':'!!'}
firstoutput = {}
try :
    firstoutput += firstinput 
    print firstoutput
except (RuntimeError, TypeError, NameError):
    print 'Opps !! type error!!'