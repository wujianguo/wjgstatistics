import webapp2
import datetime,logging
from statistics import Statistics

class MainPage(webapp2.RequestHandler):
    def get(self):
        ip = self.request.remote_addr
        uid = 'notfound'
        url = self.request.query_string
        new = Statistics(uid=uid,url=url,ip=ip,mtime=datetime.datetime.utcnow())
        new.put()
        self.redirect('https://www.google.com')
app = webapp2.WSGIApplication([('/.*', MainPage)],
                              debug=False)
