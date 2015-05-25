#coding:utf-8
#################
# 习题41:学习面向对象术语
#################
# 前言
# 
# 学习并熟悉面向对象的术语
#

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
     "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self,***)":
     "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want do drill phrases first(首先练习惯用语)
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())
    

def convert(snippet, phrase):    # 转换--把网站里的单词换到字典中代替那些符号
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]   #
    other_names = random.sample(WORDS, snippet.count("***"))    #
    results = []
    param_names = []
    
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))    #
        
    for sentence in snippet, phrase:   # 遍历这两个列表
        result = sentence[:]   
        
        # fake class names (篡改)——原bug这里的缩进出问题了。
        for word in class_names:
            result = result.replace("%%%", word, 1)
        
        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
        
        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
        
        results.append(result)
    
    return results    #返回替换完单词的列表
    
    
# keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)    # 洗牌
        
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:    # 根据PHRASE_FIRST的值来判定问答的模式
                question, answer = answer, question
                
            print question
            
            raw_input("> ")
            print "ANSWER: %s\n\n" % answer
except EOFError:
    print "\nBye"
