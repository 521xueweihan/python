#coding:utf-8
import web

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')   # 渲染templates/文件夹下的index

class Index(object):
    def GET(self):
        greeting = "Hello World"
        #return render.index(greeting = greeting # 把greeting变量传递给index网页模板中的greeting
        return render.foo(greeting = greeting)  #templates文件夹下创建了一个新的foo.html的模板
if __name__ == "__main__":
    app.run()
