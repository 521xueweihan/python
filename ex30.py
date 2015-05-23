#coding:utf-8
#################
# 习题30:else 和 if
#################
# 前言
#
# 那四个空格的意思就是：缩进块
#


people = 30
cars = 40
buses = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."
    
if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."
    
if people > buses:
    print "Alright,let's juset take the buses."
else:
    print"Fine ,let's stay home then."
    
if people > cars and people >buses:    # 这里写一些加入布尔关系式的条件
    print u"没车可作！"
elif people < cars:
    print u"做car"
else:
    print u"做bus"
    
