#coding:utf-8
#################
# 习题44b:继承--显示覆盖
#################
# 前言
# 显示覆盖

class Parent(object):
    
    def override(self):
        print "PARENT override()"
        
class Child(Parent):
    
    def override(self):
        print "CHILD override()"
        
dad = Parent()
son = Child()

dad.override()
son.override()
