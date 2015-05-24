#coding:utf-8
#################
# 习题40:模块，类和对象
#################
# 前言
# python是一门面向对象的语言。这个说法的意思是，python
# 里面有一种叫做类（class）的结构。
# 你需要明白的是：面向对象的思想，并尽快掌握它

class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        self.name = "xueweihan"    # 这就是要输出的东西
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
    
    def screech(self):    #  我在这里新增了一个方法--输出一些东西
        print "-" * 5
        print self.name
            
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
                        
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


happy_bday.screech()    # 函数的调用在这
