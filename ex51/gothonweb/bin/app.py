#coding:utf-8
import web

urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')   # 渲染templates/文件夹下的index

class Index(object):
    def GET(self):
        return render.hello_form()
        
    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting = greeting)
        
if __name__ == "__main__":
    app.run()
