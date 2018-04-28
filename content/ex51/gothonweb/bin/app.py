#coding:utf-8
import web

urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")   # 渲染templates/文件夹下的index

class Index(object):
    def GET(self):
        return render.hello_form_laid_out()
        
    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index_laid_out(greeting = greeting)
        
if __name__ == "__main__":
    app.run()
