#coding:utf-8
#################
# 习题37:复习各种符号
#################
#前言
#我把这一章详细的代码加说明写在我的博客里面了
#地址：http://www.cnblogs.com/xueweihan/

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
    
print u"输出全局变量NAME的值:", get_NAME()
new_name = "521xueweihan"
set_NAME(new_name)     # 为全局变量重新赋值
print u"输出赋值完的全局变量NMAE的值：", get_NAME() 


# 理解pass的用途
def test_pass():pass    # 如果不加pass，抛出错误：IndentationError: expected an indented block

test_pass()


# 理解yield
def test_yield(n):
    for i in range(n):
        yield i*2    # 每次的运算结果都返回
              
for j in test_yield(8):
    print j,":",
    
print u"结束理解yield"   

# 利用yield输出斐波那契数列
##########
# 看这里，太厉害了，不是我写的。。。。
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
  
    
# 理解except
try:
    num = 5/0
except:
    print u"计算出错"
    
try:  
   f = open("file.txt","r")    # 如果该文件不存在
except IOError, e:   # 捕获IO异常
   print u"IO错误！"
   print e                # 输出错误信息，这里e是错误信息
   
   
# 理解in
first_list = [1, 2]
second_list = [1, 2, 3]
element = 1
red = 'red'
red_clothes = "red clothes"
print red in red_clothes
print first_list in second_list   # false
print element in first_list      # true


# 理解raise
try:
    raise IOError    # 这里可以raise一个自定义的错误类。那样就叫做自定义异常了
    print u"是否执行?"    # 不执行
except IOError:
    print "IOError test raise"
    
    
# 理解is
e = 1
es = 1.0
ess = 1
print u"""is就是比对id的值，看是否指向同一对象，
这里需要注意的是：同一对象,不是值相等就是同一对象。"""
print id(e)
print id(es)
print id(ess)


# 理解lambda
g = lambda :"lambda test."
print g()
num1 = lambda x, y=1:x + y
print num1(1)      # 多个变量的时候，可以不给有默认值的变量传值
print num1(10,10)    # 值得注意的是，如果y没有默认值而且不给它传值的话报错！

#######
# 数据类型
#######
print True and False   # 注意首字母大写
print None == ""
print None == 0     # 注意None是特殊的一种数据类型
print "test \\b\b"  # 测试\b


#######
# 转义字符
#######
print "test \\b  :lo\bve"    # 测试\b,应该输出lve

print u"你好吗？\n朋友"    # \n 和 \b的区别
print u"——分隔线——"
print u"你好吗？\r朋友"


#######
# 字符串格式化
#######
print "%f,%F"% (3.1422222222222222222,3.1422222222222222222)   # 我没发现区别！
