#coding:utf-8
#################
# 习题29:if语句
#################
# 前言
#
# 朋友们终于到有逻辑的地方了，你们难道不兴奋吗？
#


people = 20
cats = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!"
 
if people > cats:
    print "Not many cats! The world is saved!"
    
if people < dogs:
    print "The world is drooled on!"    # 流口水
    
if people > dogs:
    print "The world is dry!"
    
    
dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."
    
if people <= dogs:
    print "People are less than or equal to dogs."
    
if people == dogs:
    print "People are dogs."
