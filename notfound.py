import webapp2
import datetime,logging
from statistics import Statistics

class MainPage(webapp2.RequestHandler):
    def get(self):
        ip = self.request.remote_addr
        uid = 'notfound'
        url = self.request.query_string
        if not url:
            url = 'http://www.baidu.com'
        s = Statistics.all()
        s.filter("uid =", uid)
        u = s.get()
        if u:
            u.url.append(url)
            u.ip.append(ip)
            u.mtime.append(datetime.datetime.utcnow())
            u.put()
        else:
            new = Statistics(uid=uid,url=[url,],ip=[ip,],mtime=[datetime.datetime.utcnow(),])
            new.put()
        if not url.startswith('http'):
            url = 'http://' + url
        self.redirect(str(url))
app = webapp2.WSGIApplication([('/.*', MainPage)],
                              debug=False)
