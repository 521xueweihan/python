#coding:utf-8
#################
# 习题44c:继承--在运行前或运行后替换
#################
# 前言
# 第三种方法是一个覆盖的特例，你想在父类中定义的内容运行之前
# 或之后再修改行为。

class Parent(object):
    
    def altered(self):
        print "PARENT altered()"
        

class Child(Parent):
    
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"
        
dad = Parent()
son = Child()

dad.altered()
son.altered()
