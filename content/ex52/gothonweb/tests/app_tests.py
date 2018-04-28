from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
# 这个是原来的test，有问题   
    
    #test Get request to /hello
    resp = app.request("/hello")
    assert_response(resp)
    
    #make sure default values work for the form
    resp = app.request("/hello", method="POST")
    assert_response(resp, contains="Nobody")
    
    #test that we get expected values
    data = {'name':'Zed', 'greet': 'Hola'}
    resp = app.request("/hello", method="POST", data=data)
    assert_response(resp, contains="Zed")
    
# 笔记
#
# 这个web游戏我还没有完全看懂，等我慢慢消化了，在回头看
# 而且我觉得这个学这个框架还不如学flash，我下一步要学这个
# 
# 但是有一点我承认我偷懒了：我应该把这个测试写好的，
# 可是我没弄懂这个程序，写测试有点难。算了，以后再说吧。
# 没准有一天在学习其他的过程中，对这个测试就突然懂了呢！
#

