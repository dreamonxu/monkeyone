import cherrypy
import os.path
current_dir=os.path.dirname(os.path.abspath(__file__))

class Root(object):
    content ="""... <omitted>... """
    @cherrypy.expose
    def index(self):
        return Root.content

if __name__ == "__main__":
    cherrypy.quickstart(Root(), config={
               '/static':
               {'tools.staticdir.on':True,
                'tools.staticdir.dir':os.path.join(current_dir,"static")
                }
                                            })
        