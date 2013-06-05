import webapp2
from google.appengine.api import users
import json
from statistics import Statistics

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user or not users.is_current_user_admin():
            self.redirect(users.create_login_url(self.request.uri))
        self.response.headers['Content-Type'] = 'application/json'
        resmsg = {'result':[]}
        infos = Statistics.all()
        for s in infos:
            one_uid = {s.uid:[]}
            for j in range(len(s.ip)):
                one_uid[s.uid].append([s.ip[j],s.url[j],s.mtime[j].strftime("%Y-%m-%d %H:%M:%S")])
            resmsg['result'].append(one_uid)
        self.response.write(json.dumps(resmsg))
app = webapp2.WSGIApplication([('/admin', MainPage)],
                              debug=True)
