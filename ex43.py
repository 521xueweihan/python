#coding:utf-8
#################
# 习题43:基本的面向对象分析和设计
#################
# 前言
# 
# 如何把现实中的问题抽象出来，并提取共同点——写成父类
# 注意考虑动词，转化为类的动作

class Scene(object):
    
    def enter(self):
        pass
        

class Engine(object):
    
    def __init__(self, scene_map):
        pass
        
    def play(self):
        pass
        
class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):
    
    def enter(self):
        pass
        
class  LaserWeaponArmory(Scene):

    def enter(self):
        pass
        
class TheBridge(Scene):
    
    def enter(self):
        pass
     
class EscapePod(Scene):

    def enter(self):
        pass
        

class Map(object):
    
    def __init__(self, start_scene):
        pass
        
    def next_scene(self, scene_name):
        pass
        
    def opening_scene(self):
        pass
        
        
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
