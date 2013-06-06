import webapp2
from google.appengine.api import users
import json, logging, datetime
from statistics import Statistics
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))
class MainPage(webapp2.RequestHandler):
    def get(self):
        ip = self.request.remote_addr
        user = users.get_current_user()
        if not user or not users.is_current_user_admin():
            self.redirect(users.create_login_url(self.request.uri))
        template_values = {'user': user,}
        sta = Statistics.all()
        uids = []
        for s in sta:
#            uids.setdefault(s.uid,[])
            uids.append({'uid':s.uid,'ip':s.ip,'mtime':s.mtime+datetime.timedelta(hours=8),'url':s.url})
#            uids[s.uid].append({'ip':s.ip,'time':s.mtime,'url':s.url})
        template_values.update({'statistics':uids})
        template = JINJA_ENVIRONMENT.get_template('admin.html')
        self.response.write(template.render(template_values))
app = webapp2.WSGIApplication([('/admin', MainPage)],
                              debug=True)
