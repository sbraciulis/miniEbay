import web

render = web.template.render('templates/')
urls = (
  '/', 'index',
  '/search', 'search',
  '/browse', 'browse'
)

class index:
  def GET(self):
    return render.index()

class search:
	def GET(self):
		return render.search()
	
class browse:
	def GET(self):
		return render.browse()
	
if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()
