#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import datetime
import logging
from statistics import Statistics


class MainPage(webapp2.RequestHandler):

    def get(self):
        ip = self.request.remote_addr
        uid = 'notfound'
        url = self.request.uri
        user_agent = self.request.headers.get('User-Agent','none')
        new = Statistics(uid=uid,url=url,user_agent = user_agent, ip=ip,mtime=datetime.datetime.utcnow())
        new.put()
        self.redirect('https://www.google.com')
app = webapp2.WSGIApplication([('/.*', MainPage)],
                              debug=False)
