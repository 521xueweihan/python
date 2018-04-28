#coding:utf-8
#################
# 习题35:分支和函数
#################
# 前言
#
# 就是逻辑和函数的综合应用，有点长不要被吓到
#

from sys import exit

def gold_room():
    print u"这个房间装满了黄金，你要拿走多少？"
    
    next = raw_input("> ")
    if "0" in next or "1" in next:    # 检测输入中是否有0或1
    #if int(next) >= 0:    # 检测输入是正数
        how_much = int(next)
    else:
        dead(u"Man, 请注意数据类型")
    
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You gready bastard!")    # 贪婪的混蛋
    
    
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
     
    while True:
        next = raw_input("> ")
        
        if next == "take honey":
            dead("The bear looks at you then slaps your face off。")   # slap:掌击
        elif next == "taunt bear" and not bear_moved:    # 你输入：嘲讽熊，别且熊移动过来
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."
            
            
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He,it ,whatever stares at you and you go insane."    # 邪神的眼睛在注视着你，你逃跑了
    print "Do you flee your life or eat your head?"
    
    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
        
        
def dead(why):
    print why, "God job!"
    exit(0)
    
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take ?"
    
    next = raw_input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
        
        
start()    # 调用start（）函数

# 笔记
#
# 字符串前面加u，对该字符串毫无影响
# 但是输入的时候还是有问题（raw_input()）
#
