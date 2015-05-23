#coding:utf-8
#################
# 习题33:while循环
#################
# 前言
#
# 介绍和使用：while
# 需要注意的是：1.尽量少用while
#			   2.while是无限循环的，只有遇到条件为false时停止
#             

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i 
    numbers.append(i)
    
    i = i + 1    # 限制while无限循环的条件
    print "Numbers now :", numbers
    print "At the bottom i is %d" % i

    
print "The numbers: "

for num in numbers:
    print num
    
# 更多练习    
print ("-"*5) + (u"更多练习") + ("-"*5)

def number_while(num, number, var ):
    i = 0
    while i < num:
        print u"数字：%d 放入number列表。" % i
        number.append(i)
        print u"number列表的数据是：", number
    
        i = i + var 

def number_for(num, number):
    for i in range(0, num):
        i = i + 3
        
        print "num is :",i
        number.append(i)
        print "number is :",number
        
    print "end"
    
    
test_number_list = []
number_for(10, test_number_list)
number_while(10, test_number_list, 2)
print i

# 笔记
#
# for循环中 i不需要定义，for自己带给i定义的功能
# while中 i 需要定义
