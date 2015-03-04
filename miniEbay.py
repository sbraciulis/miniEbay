
from web import*

urls = (

        '/','index',

)

class index:
        def GET(self):
                return "OK!"


if __name__ == "__main__":
        app=application(urls,globals())
        app.run()
