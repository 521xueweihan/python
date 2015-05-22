#coding:utf-8
#################
# 习题12:提示别人
#################
# 前言
#
# 这里主要理解：raw_input("提示信息")的用法
#

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

print "So, you are %r old, %r tall and %r heavy."% (
    age, height, weight)
