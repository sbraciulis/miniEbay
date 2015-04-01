import web

db = web.database(dbn='mysql', user='cs351', pw='pass', db='miniEbay')
render = web.template.render('templates/')
urls = (
  '/', 'index',
  '/search', 'search',
  '/browse', 'browse',
  '/results', 'results',
  '/auction', 'auction'
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

class results:
  def POST(self):
    query = web.data().split('=')[1]
    auctionList = db.select('auctions')
    results = []
    
    for auction in auctionList:
      if query.lower() in auction.title.lower().replace(" ", ""):
        results.append(auction)
      
    return render.results(results)
  
class auction:
  def GET(self):
    return render.auction()
  
if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()
