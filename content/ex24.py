#coding:utf-8
#################
# 习题24:更多练习
#################
# 前言
#
# 这个练习比较长，需要耐心，朋友看看你是不是一个有耐心的人？
# 这个练习时综合以前学过的东西写的，就像我写的ex22简化版

print "Let's pratice everthing."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

# 下面是一首我看不懂的诗
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of lovel
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "------------"
print poem
print "------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# 这个函数是：输入一个值经过计算返回三个值
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    
    
    
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of : %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We 'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
