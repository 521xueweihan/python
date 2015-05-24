#coding:utf-8
#################
# 练习应用类
#################

class Test:
    def __init__(self, name):
        self.name = name
        
x = Test(1)    
print x.name   # 这里尝试输出‘你好’————把第十行改成：x = Test(u'你好')

###################

class TestVarible:
    samething = 'Hello Word.'    # 共享的变量
    def __init__(self, name):
        self.name = name    # 每个实例独一无二的变量
    
one = TestVarible('one')
two = TestVarible('two')
print 'one:',one.name, ';Same thing:', one.samething
print 'two:',two.name, ';Same thing:', two.samething

###################

class TestError:
    tricks = []    #正确的应该是把这句移动__init__函数中或者add_tricks函数中
#   def __init__(self)：
#       
        
    def add_tricks(self,stuff):
        self.tricks.append(stuff)
        
dog1 = TestError()
dog1.add_tricks('dog1')
dog2 = TestError()
dog2.add_tricks('dog2')
print dog1.tricks,'\n----------'
print dog2.tricks    # 输出之而后你会发现tricks是共享的列表，对象的数据变成共享的了
# 这里需要注意的是：类中属性名和方法名要区别开否则会出现很难发现的错误
# 再次声明命名约定可以避免很多麻烦。
####################
