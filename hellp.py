import cherrypy
class OnePage(object):
    def index(self):
        return "one page!"
    index.exposed = True
class HelloWorld(object):
    onepage=OnePage()
    def index(self):
        return "hello world"
    index.exposed=True

cherrypy.quickstart(HelloWorld())