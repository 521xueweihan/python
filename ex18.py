#coding:utf-8
#################
# 习题18:命名，变量，代码和函数
#################
# 前言
#
# 学习使用和创建----函数
#

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1,arg2)
# 这里需要注意，用四个空格
	
# ok,that *args is actually pointless(无意义),we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this just takes one argument(参数)
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got 'nothin'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

# 笔记		
# 1.首先用def命令创建一个函数		
# 2.起函数名
# 3.加上（）里面写上参数
# 4.用：结束本行	
# 注意！5.冒号下面用4个空格缩进的行都是属于这个函数的内容
	
