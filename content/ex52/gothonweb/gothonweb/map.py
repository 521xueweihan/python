#coding:utf-8
class Room(object):

    def __init__(self, name, description):
        self.name = name 
        self.description = description
        self.paths = {}
        
    # 返回依据direction在paths中的到的值    
    def go(self, direction):
        return self.paths.get(direction, None)    
    
    # 给paths赋值   
    def add_paths(self, paths):    
        self.paths.update(paths)
        
        
central_corridor = Room("Central Corridor",
"""
行星Percal＃25 Gothons已经侵入你的飞船，销毁
了你的所有船员。你是最后生存者，你的最后
任务是从武器军械库获得中子毁灭炸弹，
把它放在桥梁，引爆它并成功进入
逃生舱逃生。

当你通过中央走廊向武器仓库跑去的时候，
一个Gothon跳出，鳞状皮肤红，黑肮脏的牙齿，和邪恶的小丑服装
流动围绕着他充满仇恨的身体。他堵大门
（The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew. You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge,and blow the ship up after getting into an
escape pod.

You're running down the central corridor to the Weapons Armory when
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
flowing around his hate filled body. He's blocking the door to the）
""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""
你是幸运的，他们让你学会Gothon侮辱的学院。
你讲一个你知道的笑话给Gothon：
Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhag gur ubhfr。
Gothon停止，尽量不笑，然后爆发出大笑，无法动弹。
在他的笑的时候你跑起来拍他的头部
把他打倒，然后跳进武器军械库的门。

你你翻身滚进武器兵工厂，蹲下以及扫描这个房间
寻找可能隐藏着的Gothons。这里死一般的安静，太安静了。
你站起来，跑到房间的另一边，并找到
获得炸弹需要的代码。如果你得到的代码
错10次那么锁将永远关闭，你就不能
拿到炸弹。代码是3位数的。
（Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know:
Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhag gur ubhfr.
The Gothon stops, tries not to laugh, then busts out laughing and can't move.
While he's laughing you run up and shoot him square in the head
putting him down, then jump through the Weapon Armory door.

You do a dive roll into the Weapon Armory, crouch and scan the room
for more Gothons that might be hiding. It's dead quiet, too quiet.
You stand up and run to the far side of the room and find the
and you need the code to get the bomb out. If you get the code
wrong 10 times then the lock closes forever and you can't
get the bomb. The code is 3 digits.）
""")


the_bridge = Room("The Bridge",
"""
该容器点击打开，密封断开，让气体出来。
你拿起中子弹和拼锦全力的跑，你可以到
桥，你必须将其放置在正确的位置。

你用胳膊夹着炸弹，5个试图占领
飞船的控制权的Gothons。他们每个人都有一个更丑陋
小丑服装对比之前。他们没有拿出自己
武器出来呢，因为他们看到在活动的炸弹
手臂，不希望被炸死。
（The container clicks open and the seal breaks, letting gas out.
You grab the neutron bomb and run as fast as you can to the
bridge where you must place it in the right spot.

You burst onto the Bridge with the netron destruct bomb
under your arm and surprise 5 Gothons who are trying to
take control of the ship. Each of them has an even uglier
clown costume than the last. They haven't pulled their
weapons out yet,as they see the active bomb under your
arm and don't want to set it off.）
""")
escape_pod = Room("Escape Pod",
"""
你全部寄托在你的胳膊夹着的原子弹
Gothons举起他们的手，开始流口水。
你快速到达门口，打开它，然后仔细地
把炸弹放置在地板上，就指着你的炸弹了。
之后你跳回到门外，按下了关闭按钮
和摧毁了锁使Gothons无法通过。
现在，炸弹被放置好了，你逃到了逃生舱，以
逃离，这个铁罐（飞船）。

你急于飞船，拼命取保飞船爆炸前
到达逃生舱。好像
几乎没有任何Gothons在船上，所以你逃跑时没有任何
干扰。你到达了逃生舱的房间，现在
需要选择一个上去。他们中的一些可能是损坏的
但你没有时间去仔细看。有艘逃生艇，你打算上
那个？
（You point your blaster at the bomb under your arm
and the Gothons put their hands up and start to sweat.
You inch backward to the door, open it, and then carefully
place the bomb on the floor, pointing your blaster at it.
You then jump back through the door, punch the close button
and blast the lock so the Gothons can't get out.
Now that the bomb is placed you run to the escape pod to
get off this tin can.

You rush through the ship desperately trying to make it to
the escape pod before the whole ship explodes. It seems like
hardly any Gothons are on the ship, so your run is clear of
interference. You get to the chamber with the escape pods, and
now need to pick one to take. Some of them could be damaged
but you don't have time to look. There's 5 pods, which on 
do you take?）
""")


the_end_winner = Room("The End",
"""
你跳进2号逃生舱，按下弹出按钮。
该逃生舱很容易滑出到太空
前往下面的星球。当它飞向地球时，你回头
看，会发现你的船爆炸时像
一颗明亮的星星，于此同时逃出了Gothon的飞船。你赢了！
（You jump into pod 2 and hit the ejext button.
The pod easily slides out into space heading to
the planet below. As it flies to the planet, you look
back and see your ship implode then explode like a
bright star, taking out the Gothon ship at the same
time. You won!）
""")


the_end_loser = Room("The End",
"""
你随机跳进一个逃生舱按下弹出按钮。
该逃生舱掉进了空间空隙，然后
船体破裂爆炸了，你的身体粉碎成了
果酱果冻。
（You jump into a random pod and hit the eject button.
The pod escapes out into the void of space, then
impolodes as the hull ruptures, crushing your body
into jam jelly.）
""")

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

generic_death = Room("death", "You died.")

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '0132': the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke': laser_weapon_armory
})

START = central_corridor
