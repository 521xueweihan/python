#coding:utf-8
#################
# 习题4:变量和命名
#################
# 前言
#
# 变量就像名字，用来方便的代表某个东西


# 变量名
#
# 汽车有100
#
# 每辆车能做4个人
#
# 有30个司机
#
# 乘客90人
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_drvien = cars - drivers  # 有车没司机的数量
cars_driven = drivers             # 有车有司机的数量
carpool_capacity = cars_driven * space_in_a_car  # 所有能走的车加起来座位的数量
average_passengers_per_car = passengers / cars_driven  # 每辆车几个人

# 我要先歇会——————14：54
# gogo——20：25
print "There are", cars, "cars available."# 这里有 100 辆车可用
print "There are only", drivers, "drivers available."# 这里有 30 位司机可用
print "There will be", cars_not_drvien, "empty cars today."
print "We can transport", carpool_capacity, "people today."# 我们可以运输 人
print "We have", passengers, "to carpool today."# 我们有90位乘客
print "We need to put about", average_passengers_per_car, "in each car."# 每辆车放多少人

# 笔记
#
# 如果计算式子中有浮点数结果必然为浮点数
print "4.0 + 3=", 4.0 + 3
