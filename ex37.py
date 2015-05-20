#coding:utf-8
#################
#习题37:复习各种符号
#################
#前言
#

#熟悉global

#定义全局变量，变量名全部大写
NAME = "xueweihan"

#得到NAME值
def get_NAME():
    return NAME

#重新设定NAME值
def set_NAME(name_value):
    global NAME
    NAME = name_value
    
print u"输出全局变量NAME的值:",get_NAME()
new_name = "521xueweihan"
set_NAME(new_name)#为全局变量重新赋值
print u"输出赋值完的全局变量NMAE的值：",get_NAME() 


#理解pass的用途
def test_pass():pass  #如果不加pass，抛出错误：IndentationError: expected an indented block

test_pass()


#理解yield
def test_yield(n):
    for i in range(n):
        yield i*2#每次的运算结果都返回
              
for j in test_yield(8):
    print j,":",
print u"结束理解yield"   
#利用yield输出斐波那契数列
##########
#看这里，太厉害了，不是我写的。。。。
##########
def fab(max):
    a,b = 0,1
    while a < max:
        yield a
        a, b = b, a+b
print u"斐波那契数列！"
for i in fab(20):
    print i,",",
print u"斐波那契数列结束。"
    
#理解except
try:
    num = 5/0
except:
    print u"计算出错"
    
try:  
   f = open("file.txt","r")  #如果该文件不存在
except IOError, e:  #捕获IO异常
   print u"IO错误！"
   print e                #输出错误信息，这里e是错误信息
   
#理解in
first_list = [1, 2]
second_list = [1, 2, 3]
element = 1
red = 'red'
red_clothes = "red clothes"
print red in red_clothes
print first_list in second_list  #false
print element in first_list      #true

#理解raise
try:
    raise IOError #这里可以raise一个自定义的错误类。那样就叫做自定义异常了
    print u"是否执行?" #不执行
except IOError:
    print "IOError test raise"
    
    
#理解is
e = 1
es = 1.0
ess = 1
print u"""is就是比对id的值，看是否指向同一对象，
这里需要注意的是：同一对象,不是值相等就是同一对象。"""
print id(e)
print id(es)
print id(ess)

#理解lambda
