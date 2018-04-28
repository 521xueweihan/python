#coding:utf-8
from nose.tools import *
from gothonweb.map import *
# 在ex52项目的gothonweb文件夹下面——输入：nosetests
# nose是指令，tests--是执行nose指令的文件夹
# tests文件夹中的xx_tests.py文件就是测试文件，
# 里面有几个函数就测试就是几个测试用例
def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""")                
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})
    
def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")
    
    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)    # 用断言判断两个值是否相等
    
def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here,you can go up.")
    
    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})
    
    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_gothon_game_map():
    assert_equal(START.go('shoot!'), generic_death)
    assert_equal(START.go('dodge!'), generic_death)
    
    room = START.go('tell a joke')
    assert_equal(room, laser_weapon_armory)    
# 笔记    
# 1.测试脚本要放在test/目录下，并且命名为xx_tests.py,否则nosetests就不会执行
# 你的测试脚本了。这样还有一个好处就是防止测试代码和别的代码互相混掉。
# 2.为你的每一个模块写一个测试。
# 3.测试用例（函数）保持简短，但如果看上去不怎么整洁也没关系，测试用例一般都有点乱。
# 4.就算测试用例有些乱，也要试着让他们保持整洁，把里面的重复代码删掉。创建一些辅助
# 函数来避免重复的代码。因为重复的代码会让修改测试变的十分困难
# 5.最后一条是别把测试当回事。有时候，更好的方法是把代码和测试全部删掉
# 然后重新设计代码。——好的代码不是一次就写出来的    
