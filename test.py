#coding:utf-8
#####
#这个文件时联系基本语法规则
#简称：默写本！
#####
from sys import argv
#联系一下默写，文件拷贝
script,from_file,in_file = argv

file = open(from_file)#这句原来写错了，写成了from_file.open
indate = file.read()

files = open(in_file,'w')#还有这句
files.write(indate)

files.close()#注意：关闭时关闭open的对象
file.close()
####################
#coding:utf-8
#####
#这个文件时联系基本语法规则
#简称：默写本！
#####
#from sys import argv

def save_money(money, days):
    print u"你存了：%d元" % money
    print u"打算存：%d天" % days
    print u"每天给你：10元做利息！（我没开玩笑）"
    print "wait.....one day,two day......"
    print u"这些是给你的：%d." % (money+days*10)
	
#script, input_money, input_days = argv
input_money = int(raw_input("How much do you want save?"))#这里输出中文有问题
input_days = int(raw_input("For How long?"))
save_money(input_money, input_days)