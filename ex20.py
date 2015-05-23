#coding:utf-8
#################
# 习题20:函数和文件
#################
# 前言
#
# 函数和文件的协作使用
#

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()
	
# 回归文件的开头
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline(),

current_file = open(input_file)     # 当前文件

print "First let's print the whole file:\n"

print_all(current_file)   	

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
