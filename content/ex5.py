#coding:utf-8
#################
# 习题5:更多的变量和打印
#################
# 前言
#
# 格式化字符串主要作用是：
#
# 使用专门的格式和语法把变量的内容放到字符串里。
#
# %d输出数字 
# %s输出字符串


my_name = 'XueWeiHan'
my_age = 22
my_height = 170 # cm
my_weight = 60 # kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d kg heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# 这里是有错误的，找出错误
print "If I add %d,%d,and %d I get %d" %(
    my_age, my_height, my_weight, my_age + my_height + my_weight)  
# 我没找到错误！
