#coding:utf-8
#################
# 习题21:函数可以返回某些东西
#################
# 前言
#
# 函数使用return返回值
#

def add(a, b):
    print "ADDING %d +%d" % (a, b)
    return a + b
    
# 减法
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)    
    return a - b
    
def multiply(a, b):
    print "MULTIPLY %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDE %d / %d" % (a, b)
    return a / b    
    
print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d " % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# 由内而外调用函数计算结果
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
