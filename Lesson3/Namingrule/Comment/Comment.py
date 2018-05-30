# -*- coding: utf-8 -*-
'''
這裡我使用了四個變數, 分別代表了年齡, 姓氏, 名稱與技能
'''
#這是年齡, 它是字串
MyAge = 34
#這是姓氏, 它是字串
LastName = 'Chen'
#這是名稱, 它是字串
FirstName = 'Mir'
#這是技能, 它是列表
MyProgramingSkillList = ['Python','C','C++']


print 'Hi guys, '
print 'my name is : ' + FirstName + ',' + LastName + '.'
print 'I am ' + str(MyAge) + ' ' + 'years old.'
print 'I have following skill for programing : '
for skills in MyProgramingSkillList : 
    print skills