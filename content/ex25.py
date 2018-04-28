#coding:utf-8
#################
# 习题25:更多更多的实践
#################
# 前言
#
# 我有一个愿望：希望以后尽可能少的出现我看不懂的诗。
# 我觉得应该给每个方法写上注释，所以我就写了如下注释
#

# break_words：把输入的句子依据空格分隔成单个单词
def break_words(stuff) :
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

# sort_words:依据首字母顺序给单词排序    
def sort_words(words):
    u"""Sorts(分类) the words."""
    return sorted(words)

# print_first_word：输出第一个单词    
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

# print_last_word：输出(并移出)最后一个单词
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word
    
# sort_sentence：把句子分隔成单词，并进行排序    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sorted(words)

# print_first_and_last：把句子分隔成单词，并输出第一个和最后一个单词
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

# print_first_and_last_sorted：把句子分隔成单词,输出第一个和最后一个单词，最后排序    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
