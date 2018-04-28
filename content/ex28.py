#coding:utf-8
#################
# 习题28:布尔表达式练习
#################
# 前言
#

man = u"男人"
woman = u"女人"
sex = man == woman
print sex    # 结果是false

print man and woman
print "test1" and "test2"    # 警告：我和书上产生了奇异，我输出的第二个操作数，书中说是第一个

# 笔记
# 书中布尔表达式的结果如下：
# 1-5:T.F.F.T.T 
# 6-10:T.F.T.F.F
# 7-15:T.F.T.F.F
# 16-20:F.T.T.F.F
#

