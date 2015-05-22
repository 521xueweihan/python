#coding:utf-8
#################
# 习题13:参数,解包和变量
#################
# 前言
#
# 另外一种将变量传递给脚本的方法，
#
# 写一个可以接受参数的脚本

from sys import argv

script, first, second, third = argv

print "The script is called :", script
print "Your first variable is :", first
print "Your second variable is :", second
print "Your third variable is :", third

# 笔记
# 1.这里初步体验了python引入模块的方法
# 2.先感受一下，后面才是正菜
# 3.运行这个脚本的时候：
#python ex13.py first 2nd 3rd(后面三个是传递的参数)
