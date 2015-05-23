#coding:utf-8
#################
# 习题31:做出决定	
#################
# 前言
#
# 练习一下:if
#

print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1.Take the cake."
    print "2.Scream at the bear."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off. God job!"
    elif bear == "2":
        print "The bear eats your legs off. God job!"
    else:
        print "Well, doing %s is probably better.   Bear runs away." % bear
        
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. God job."
    else:
        print "The insanity rots your eyes into a pool of muck. God job."

# 这里是我增加的功能       
elif door == "3":
    print u"发现一只熊猫！"
    print u"1.说：你好!"
    print u"2.说：Hello"
    
    words = raw_input("> ")
    
    if words == "1":
        print u"熊猫很友好！"
    else:
        print u"你说啥嘞，弄死你！"
else:
    print "You stumble around and fall on a knife and die. God job."
    
# 如果看完第一遍你有些发晕
# 那你就画一个流程图（不懂百度一下--强行植入广告）看看
#
