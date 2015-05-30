#coding:utf-8
class Room(object):

    def __init__(self, name, description):
        self.name = name 
        self.description = description
        self.paths = {}
        
    #返回依据direction在paths中的到的值    
    def go(self, direction):
        return self.paths.get(direction, None)    
    
    #给paths赋值   
    def add_paths(self, paths):    
        self.paths.update(paths)
