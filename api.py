import webapp2
from google.appengine.api import users
import json
from statistics import Statistics

class MainPage(webapp2.RequestHandler):
    def get(self):
        ip = self.request.remote_addr
        self.response.headers['Content-Type'] = 'application/json'
        resmsg = {'errcode':'ok','result':[]}
        resmsg['result'].append({'ip':ip})
        self.response.write(json.dumps(resmsg))
app = webapp2.WSGIApplication([('/api', MainPage)],
                              debug=True)
