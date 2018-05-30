# -*- coding: utf-8 -*-
import sys

# 60 = 0011 1100 
fisrtvariable = 60 
print bin(fisrtvariable)

# 13 = 0000 1101 
secondvariable = 13       
print bin(secondvariable)

# 0 = 0000 0000
thirdvariable = 0
print bin(thirdvariable)

# 12 = 0000 1100
thirdvariable = fisrtvariable & secondvariable
print "Line 1 - Value of c is ", thirdvariable

# 61 = 0011 1101
thirdvariable = fisrtvariable | secondvariable 
print "Line 2 - Value of c is ", thirdvariable

# 49 = 0011 0001
thirdvariable = fisrtvariable ^ secondvariable
print "Line 3 - Value of c is ", thirdvariable

# -61 = 1100 0011
thirdvariable = ~fisrtvariable;
print "Line 4 - Value of c is ", thirdvariable

# 240 = 1111 0000
thirdvariable = fisrtvariable << 2;
print "Line 5 - Value of c is ", thirdvariable

# 15 = 0000 1111
thirdvariable = fisrtvariable >> 2;
print "Line 6 - Value of c is ", thirdvariable