#coding:utf-8
#################
# 习题36:测试与调试
#################
# 前言
#
# 家庭作业：
# 写这个游戏，写的挺快的
# 就是后期遇到了个逻辑bug
# 用了很长时间才铲除掉
#
# 好了，let play game吧
#

import random    # 导入随机数

print ("-"*5) + (u"更多练习") +("-"*5)

# 选择武器并跳转到challeng方法
def weapon():
    treasure = "none"
    print u"选一个你喜欢的武器吧！"
    print u"""有以下三种：
    1.刀
    2.枪
    3.棒棒糖
    """
    next = raw_input("> ")
    
    if next == "1" or next == "2":
        challenge(treasure)
    elif next == "3":
        print u"朋友是叫你来打怪兽的，你选棒棒糖？"
        weapon()
    else:
        print u"你选的啥？重来！"
        print "-----------"
        weapon()
        
# 选择挑战的内容，treasure参数是宝物的值：none和boom
# boom只能在dog房打到，有了boom才能打死bos
def challenge(treasure):   
    print u"你打算挑战那个？"
    print """
    1.Bos
    2.Dog
    """
    next = raw_input("> ")
    if next == "1":
        print "debug:",treasure
        bos_room(treasure)
    elif next == "2":
        treasure = dog_room()
    else:
        print u"你选的啥？重来！"
        print "-----------"
        challenge(treasure)
        
# 爆宝的方法，利用随机函数random，随机产生boom或者none，并把treasure参数传给challenge
def get_treasure():

    treasure = random.choice(["boom","none"])    # 随机产生boom或者none
    
    if treasure == "boom":
        print u"恭喜!你获得了无敌的存在：核弹.\n咔咔咔......\n 你装备上了核弹，可以去秒杀bos了!"    
        challenge(treasure)
        #return treasure  # 就是这里出错了!!!不需要return 直接把treasure的值给challenge就好了         
    else:
        print u"你什么都没有获得！\n"
        challenge(treasure)
        
# dog_room方法           
def dog_room():
    treasure = "none"
    print u"这里有只恶狗！"
    print u"你的动作是什么？"

    next = raw_input("a or r-> :")  
    
    if next in "a":        
        print "dog is dead.God Job!" 
        get_treasure()        
    else:
        challenge(treasure)
        
# bos_room方法   
def bos_room(treasure):
    print treasure
    print u"你面前是一个大bos！！十分大"
    print u"你的动作是什么？"
    
    next = raw_input("a or r-> :")
    
    if next == "a":
        win(treasure)
    elif next == "r":
        print u"你逃跑了"
        challenge(treasure)
    else:
        challenge(treasure)  
             
# 判断是否胜利：传入参数为treasure，如果为boom：胜利 否则失败跳转到weapon       
def win(treasure):
    if treasure == "boom":
        print u"你用核弹秒杀了bos！"
        print u"你已经通关了，再见。"
        exit(0)
    else:
        print u"你被bos打死了，快去dog房刷武器吧！"
        weapon()
        
weapon()    # 游戏开始！

# 笔记
#
# 作者在书上给了一些很好的编程习惯，
# 我去整理一下再放过来！
#
######
# If语句的规则：
  # 1.每一条if语句必须包含一个else
  # 2.如果这个else永远都不应该被执行到，因为它本身没有任何意义，那你必须在else语句后面使用一个叫die的函数，让它打印出来错误信息并且“死”给你看。
  # 3.if语句的嵌套不要超过两层，最好尽量保持只有一层。这意味着，如果你在if里面又有一个if，那你就需要把第二个if移到另一个函数里面。
  # 4.你的布尔测试应该很简单，如果它们很复杂，你需要将它们的运算事先放到一个变量里，并且为变量取一个好名字。

# 循环的规矩：
  # 1.只有循环永不停止时使用“while循环”，这意味着你可能永远都用不到。
  # 2.其他类型的循环都是用for循环，尤其是在循环的对象数量固定或者有限的情况下。
#######
