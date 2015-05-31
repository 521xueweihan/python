#coding:utf-8
from nose.tools import *
from ex49.ex49 import *
# 输入nosetests，开始测试一个
# 输出结果如下：
# qq@qq-virtual-machine:~/git/projects/skeleton$ nosetests
# ....
# ----------------------------------------------------------------------
# Ran 4 tests in 0.004s
#
# OK

def test_Sentence():
    sentence = Sentence(('noun', 'apple'), ('verb', 'eat'), ('direction', 'good'))
    assert_equal(sentence.subject, 'apple')
    
def test_peek():
    #sentence = Sentence(('noun', 'apple'), ('verb', 'eat'), ('direction', 'good'))
    peek1 = peek([('noun', 'apple'), ('verb', 'eat'), ('direction', 'good')])
    peek2 = peek([('direction', 'good')])
    peek3 = peek([])
    assert_equal(peek1, 'noun')
    assert_equal(peek2, 'direction')
    assert_equal(peek3, None)   # None != 'None'
    
def test_match():
    match1 = match([('verb', 'eat'), ('noun', 'apple')], 'verb')    #match接收的是word_list
    assert_equal(match1, ('verb', 'eat'))
    
# 我觉得的parse_verb()方法不是需要测试——因为它还调用了别的方法（不知道我想的对不对）
#def test_parse_verb():
#    parse_verb1 = parse_verb([('noun', 'apple'), ('verb', 'eat'), ('direction', 'good')])
#    assert_equal(parse_verb1,)

    
def test_parse_subject():
    last_sentence = Sentence(('', ''), ('', ''), ('', ''))
    #下面的方法返回 Sentence(subj, verb, obj)
    last_sentence = parse_subject([('verb', 'eat'), ('direction', 'nice')], ('noun', 'apple'))  
    
    assert_equal(last_sentence.verb, 'eat')
