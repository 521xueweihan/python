#coding:utf-8
#################
# 习题32:循环和列表
#################
# 前言
#
# 介绍和使用：list和for
# 我们将用循环创造一些列表
#

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'orange', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# 第一种循环输出列表的方法
for number in the_count:
    print "This is count %d" % number

# 和上面一样
for fruit in fruits:
    print "A fruit of type: %s" % fruit
    
# 列表中的内容也可以是混合的
# 注意：我们用%r 是因为我们不确定列表里面是什么
for i in change:
    print "I got %r" % i

# 我们建一个空的列表
elements = []

# 然后用range方法把0-5放进去
# 这里注意:range到6 其实是5
for i in range(0, 6):
    print "Adding %d to the list." % i
# append方法是list自带的
    elements.append(i)
    
# 现在我们输出新建的列表
for i in elements:
    print "Element was: %r" % i
    
# 在新建一个空列表
new_elements = []

# 不用for循环直接赋值
new_elements.append(range(0, 6))    # 这种赋值方式就变成了二维列表，试试只输出0

# 输出它
for i in new_elements:
    print u"列表的内容是：%r" % i
    
# 输出一个
print "one: %r" % new_elements[0][0] # 二维列表输出
print "one: %d" % elements[0]

# 笔记
# 1.range方法返回的是一个列表
# 2.步长2：range(1,5,2)
# 3.for后面加else：，总是在循环最后（结束）执行
