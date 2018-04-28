#coding:utf-8
#################
# 习题17:更多文件操作
#################
# 前言
#
# 编写一个python脚本：
# 实现复制文件
#

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)    #这个文件多大

print "Does the output file exist? %r" % exists(to_file)    #输出的文件是否存在
print "Ready , hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')    # 这里需要注意下写的模式下不可以读
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
