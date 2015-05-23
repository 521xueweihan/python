#coding:utf-8
#################
# 习题22:到现在你学会了些什么？
#################
# 前言
#
# 重温一下以前学到的
#

# 1.输出
print "hello world!"

# 2.注释
print u"你可以看到这句话"
# print u"在这句话前面加上#试试看"

# 3.数字和数字计算
print 2 + 3
print 3 < 5

# 4.变量和命名
name = u"姓名:削微寒 " 
age = u"age=15"
print "name+age: ", name+age

# 5.更多的变量和打印
print "Say a number!"
number = 100
print "The number is %d" % number
print "Tell me some somthing important!"
important_things = "I will go to the University"
print "Just say it : %s " % important_things
# 这里可以把 %s和%d 换成%r 试试看输出什么样

# 6.字符串和文本
first_name = 'Mike'
second_name = ' Jodan'
your_name = first_name + second_name
print "What your name %r ?" % your_name
print your_name

# 7.更多打印
# 注意在print后面加，就不会输出自带的换行
tip = "Congratulation You get:"
money_type = '$'
money = 100
print ("%s %s%d\n" % (tip, money_type, money))*10,
print "Now you have :", money_type, money*10

# 8.打印打印
formatter = "%s %s %s"
print formatter % (u'我', u'是', u'谁')

# 9.打印打印打印
print """ your_name
        your_name
your_name
 """
# 10.转义字符
print "\n \\  \a\a"

# 11.接收输入
print "Before: ", your_name
your_name = raw_input("Input a new name.")
print "Now :", your_name

# 12.导入模块实现接收
#from sys import argv
#script, frist_name, second_name= argv
#print script + frist_name+ second_name

# 13.读取文件
from sys import argv

script, file_name = argv
# 这个函数是实现文件的输出
def file_output(file_name):
    file_data = open(file_name)
    indata = file_data.read()
    print indata 
  
# 函数实现：回退到文件的开头
def rewind(file_object):
    file_object.seek(0)
    
# 函数实现随便输出文件中的第几行   
def file_return(readline,file_object):
    rewind(file_object)
    print readline, file_object.readline()
    
file_object = open(file_name, 'a+')    # 这里需要注意的是：写的模式下不可以读

# 14.读写文件
file_object.write(your_name)
file_output(file_name)
line = 4    # 改一下这个数，看看你发现了什么
file_return(line, file_object)
# 我这个方法写的有问题，应该把rewind方法单独出来，否则每次
# 调用的时候，输出的都是第一行。
file_object.close()
# 这里的意思是：函数应该每次只干一件事情
#print file_object.read()



