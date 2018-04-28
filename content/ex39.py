#coding:utf-8
#################
# 习题39:可爱的字典
#################
# 前言
#
# 区别列表和字典：
# 1.列表：['apple', 'orange'],只可以用数字来索引元素
# 2.字典：{'name': xue, 'age': 22}，不仅可以通过数字索引，还可以通过字符串索引

# create a mapping of state to abbreviation(缩写)
states = {    # 注意书上这里出错了:字典应该是{}不是[]
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of state and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
} 

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10 
print "NY State has: ",cities['NY']
print "OR State has: ",cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is :", states['Michigan']
print "Florida's abbreviation is :", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ",cities[states['Michigan']]    # 字典可以通过变量来索引
print "Florida has: ",cities[states['Florida']]
 
# print every state abbreviation(缩写)
print '-' * 10 
for state, abbrev in states.items():    # 两个变量分别赋值为states字典中的键，值
    print "%s is abbreviated %s" % (state, abbrev)
    
# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev,city)
 
# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])
        
print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)     # get() 函数返回指定键的值，如果值不在字典中返回默认值。

if not state:    # 这里是判断state是否有值
    print "Sorry, no Texas."
    
# get a city with a default value
city = cities.get('TX', 'Does Note Exist')
print "The city for the state 'TX' is: %s" % city

# 笔记
# 1.注释的时候先打一个空格
# 2.get()函数返回指定的值,如果值不在字典中返回默认值.-----city = cities.get('TX', 'Does Note Exist')
# 3.字典是{} 不是 []
# 4.if not 是判断是否有值(或者是否为None),没有值执行代码块
x = None
if not x:
    print "x is empty"
