#coding:utf-8
#################
# 习题44e:合成
#################
# 前言
#

class Other(object):
    
    def override(self):
        print "OTHER override()"
        
    def implicit(self):
        print "OTHER implicit()"
        
    def altered(self):
        print "OTHER altered()"
        
class Child(object):
    
    def __init__(self):
        self.other = Other()    # 主要理解这里——类的合成
        
    def implicit(self):
        self.other.implicit()
        
    def override(self):
        print "CHILD override()"
        
    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"
        
son = Child()

son.implicit()
son.override()
son.altered()

# 笔记
# 继承与合成就是为了解决关于代码复用的问题
# 继承可以让你在基类里隐含父类的功能
# 合成是利用模块和别的类中的函数调用达到了代码复用的问题

# 需要注意的是：
# 1.不惜一切代价避免多重继承，因为他会带来很多麻烦。如果非要用
# 那就要准备好专研类的层次记过，以及花时间去找各种东西得来龙去脉
# 2.如果有一些代码会在不同位置和场合应用到，那就用合成来吧他们做成模块
# 3. 只有代码之间有清楚的关联，可以通过一个单独的共性联系起来的时候使用
# 继承，或者受现有代码或者别的不可抗拒因素所限非用不可，那就用吧！
#
#

