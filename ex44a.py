#coding:utf-8
#################
# 习题44a:继承--隐式继承
#################
# 前言
# 隐式继承

class Parent(object):
    
    def implicit(self):
        print "PARENT implicit()"
   
class Child(Parent):
    pass
    
dad = Parent()
son = Child()

dad.implicit()
son.implicit()
