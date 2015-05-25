#coding:utf-8
#################
list1 = ['1', '1']
list2 = ['A','B']

for x in list1, list2:
    reslut = x[:]
    print reslut    # type=list

print "---------"

print list1, list2

print "#############"
# 简单版
dir = {'A': 'a',
       'B': 'b'}
       
xq = dir.keys()
yw = dir.values()

# 这段代码是遍历两个列表之后赋值给新的两个列表
for i in xq, yw:
    answer, question = i[:]    # 这里可以加代码对元素操作之后再赋值给新的列表
    print answer, ",", question  

print "---------"
# 复杂版
for j in xq:
    answer_ = j[:]
    print answer_, ",",
    
print "\n"

for k in yw:
    question_ = k[:]
    print question_, ",",
    
