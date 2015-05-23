#coding:utf-8
#################
# 习题16:读写文件
#################
# 前言
#
# 熟悉一下方法
# close--关闭文件
# read--读取文件内容
# readline--读取文本文件中的一行
# truncate--清空文件
# write(stuff)--将stuff写入文件
#

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename    #抹去
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w+')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# 替换上面的写入
# target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
print "And finally, we close it."
target.close()

# 笔记
#
# open方法有很多模式：
# 'r'——读取
# 'w'——写入
# 'a'——追加
# 提示：'w+'等可以同时用读写的方式打开
