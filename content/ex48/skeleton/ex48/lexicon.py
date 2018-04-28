#coding:utf-8
#class lexicon(object):
# 我这里写错了，其实不应该写成类。应该是一个方法，根据模块调用的方法
           
    #@staticmethod    # 修饰为静态方法，调用时不惜要实例化
def scan(stuff):
    result = []
    direction = ['north', 'east', 'south']
    verb = ['go', 'kill' , 'eat']
    stop = ['the', 'in', 'of']
    noun = ['bear', 'princess']
    stuff = stuff.split()
    for i in range(len(stuff)):    # 如果w变量遍历整个列表，那么列表中元素是什么对象
        if stuff[i] in direction:   # w也就对应的是该对象
            d = ('direction', stuff[i])
            result.append(d)
            #return result
               
        elif stuff[i] in verb:
            v = ('verb', stuff[i])
            result.append(v)
            #return result
                
        elif stuff[i] in stop:
            s = ('stop', stuff[i])
            result.append(s)
            #return result
                
        elif stuff[i] in noun:
            n = ('noun', stuff[i])
            result.append(n)
            #return result
                
        elif convert_number(stuff[i]):    # 检测输入是否为数字
            num = ('number', int(stuff[i]))
            result.append(num)
            #return result
                
        else:
            error = ('error', stuff[i])
            result.append(error)
            #return result
    return result    # 最后返回result列表——因为有可能分割出多个word
        
def convert_number(s):    # 如果s能转化为数字则为T，不能则为F
    try:
        return int(s)
    except ValueError:
        return None                    
