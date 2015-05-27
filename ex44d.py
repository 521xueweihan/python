#coding:utf-8
#################
# 习题44d:继承--三种方式组合使用
#################
# 前言
# 第三种方法的混合使用

class Parent(object):
    
    def override(self):
        print "PARENT override()"
        
    def implicit(self):
        print "PARENT implicit()"
        
    def altered(self):
        print "PARENT altered()"
        
class Child(Parent):

    def override(self):
        print "CHILD, override()"
        
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"
        
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
