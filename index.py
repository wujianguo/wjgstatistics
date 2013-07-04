#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import datetime
import logging
from statistics import Statistics


class MainPage(webapp2.RequestHandler):

    def get(self):
        ip = self.request.remote_addr
        user_agent = self.request.headers.get('User-Agent','none')
        try:
            url = self.request.query_string
            logging.info(url)
            uid, url = url.split('&', 1)
        except Exception as e:
            logging.error(e)
            uid = 'err'
            new = Statistics(uid=uid,url=url,user_agent = user_agent, ip=ip,mtime=datetime.datetime.utcnow())
            url = 'https://www.google.com'
        else:
            new = Statistics(uid=uid,url=url,user_agent = user_agent, ip=ip,mtime=datetime.datetime.utcnow())
        new.put()
        if not url.startswith('http'):
            url = 'http://' + url
        self.redirect(str(url))
app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=False)
