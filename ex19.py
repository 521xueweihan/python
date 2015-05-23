#coding:utf-8
#################
# 习题19:函数和变量
#################
# 前言
#
# 注意：函数里的变量和脚本里的变量之间没有联系的
# 你可以用一下几种方式进行传参（给函数赋值）
#

# 奶酪和饼干
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes_of_crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"    # 毯子
	

print u"We can just give the function numbers directly（直接的）:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"    # 可以使用脚本中的变量给函数传参
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print u"And we can combine(结合) the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)	
