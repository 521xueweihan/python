#coding:utf-8
#################
# 习题42:对象，类以及从属关系
#################
# 前言
# 
# 分清什么是is—a（是什么）和has-a（有什么）
#

## Animal is-a object (yes, sort of confusing-分类是扑朔迷离的)look at the extra credit
class Animal(object):
    pass
    
## Dog is-a Animal
class Dog(Animal):
    
    def __init__(self, name):
        ## Dog has-a name
        self.name = name
        
## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name
        
## Person is-a object
class Person(object):
    
    def __init__(self, name):
        ## Person has-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None
        
## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## 继承父类的name属性
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary
        
## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass
   
    
## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

##  mary has-a pet satan is-a Cat
mary.pet = satan

## frank is-a Employee(Person) has-a salary of 120000 and super with Person 
frank = Employee("Frank", 120000)

## frank has-a pet,pet has-a name rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a Salmon kind of Fish
crouse = Salmon()

## harry is-a Halibut kind of Fish
harry = Halibut()

# 笔记
# 1.关于class Name(object)
# 在python中用到‘类即是对象’的概念，就相当于‘object’是所有类的‘父类’
# 所有的类都是继承于‘object’
# 2.super的作用体现在多重继承是，同一父类用super调用的话，不会重复出现
