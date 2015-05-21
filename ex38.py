#coding:utf-8
#################
#习题38:列表的操作
#################
#前言
#
#在对list操作的时候，python的工作原理：
#mystuff.append('hello')
#实际上是mystuff.append(mystuff,'hello')

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)
  
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]#列表倒数第一个元素
print stuff.pop()#列表最后一个元素移除
print " ".join(stuff)
print len(stuff)#join函数没有增加元素，只是输出时加入了''中的符号
print '#'.join(stuff[3:5)#[3:5]是第三个和第四个元素（要头不要尾）