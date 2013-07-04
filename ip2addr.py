#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from statistics import Statistics
import addr
class MainPage(webapp2.RequestHandler):
    def get(self):
        sta = Statistics.all()
#        sta.order("-mtime")
        for s in sta:
            if not s.addr:
                s.addr = addr.ip2addr(s.ip)
                s.put()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('ok')
app = webapp2.WSGIApplication([('/tasks/ip2addr', MainPage)],
                              debug=True)
