#coding:utf-8
#################
# 习题43:基本的面向对象分析和设计
#################
# 前言
# 
# 如何把现实中的问题抽象出来，并提取共同点——写成父类
# 注意考虑动词，转化为类的动作
#
# 场景： 死亡（Death）
#       中央走廊（Central Corridor） 需要要讲一个笑话
#       激光武器库（Laser Weapon Armory） 这会获得一个boom
#       飞船主舱（The Bridge） 在这里埋炸弹
#       救生舱（Escape Pod） 在这里逃跑
class Scene(object):
    
    def enter(self):
        print u"这个场景还没有初始化好。"
        exit(1)
        

class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map    # 这里运用了类的合成
        
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
            print "\n---------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        
class Death(Scene):    # 每个场景都是继承Scene类

    def enter(self):
        print u"你死了，GameOver！"
        exit(1)

class CentralCorridor(Scene):
    
    def enter(self):
        print u"勇士你好，这里是游戏的开始，你已经来到了飞船的“中央走廊”。这里\n"
        print u"这里被重兵把手着，你想要做些什么？"
        print u"1.开抢"
        print u"2.逃跑"
        print u"3.将一个笑话"
        
        active = raw_input("What you active?-> ")
        
        if active == "1":
            return "death"
        elif active == "2":
            return "central_corridor"
        elif active == "3":
            return "laser_weapon_armory"
        else:
            print "Wrong Number!Try again."
            
class  LaserWeaponArmory(Scene):

    def enter(self):
        print u"这里是激光武器仓库"
        print u"你得到了一个可以毁灭这艘飞船的炸弹，请妥善保存。"
        print u"快去把炸弹放在飞机主控仓"
        return 'the_bridge'
        
        
class TheBridge(Scene):
    
    def enter(self):
        print u"你来到飞机主控舱。"
        print u"放下炸弹。"
        return "escape_pod"
class EscapePod(Scene):

    def enter(self):
        print u"恭喜你，你成功的逃跑了！"
        exit(1)

class Map(object):
    
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'death': Death(),
        'escape_pod': EscapePod(),
        'the_bridge': TheBridge()
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene
        print u"勇士欢迎你，这里是%s房间。" % self.start_scene
        
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
        
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

# 笔记
# 这个游戏我只写了简单般，你可以把他扩充的难一些
# 这个游戏我不是自己写的，有的地方还是没有看懂
# 等学了下面的知识再回来看
