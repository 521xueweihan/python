#coding:utf-8
import web
from gothonweb import map

urls = (
    '/game', 'GameEngine',
    '/', 'Index'
)

app = web.application(urls, globals())

if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'room': None})
    web.config._session = session
else:
    session = web.config._session
    
render = web.template.render('templates/', base="layout")   # 渲染templates/文件夹下的index

class Index(object):
    def GET(self):
        session.room = map.START
        web.seeother("/game")        
    
    
class GameEngine(object):
    
    def GET(self):
        if session.room:
            return render.show_room(room=session.room)
        else:
            return render.you_died()
    
    def POST(self):
        form = web.input(action=None)
        # 据说这里有个bug 我没发现
        if session.room and form.action:
            session.room = session.room.go(form.action) 
        web.seeother("/game")   
if __name__ == "__main__":
    app.run()
