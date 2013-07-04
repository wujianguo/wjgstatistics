#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.redirect('http://github.wujianguo.org/favicon.ico')
app = webapp2.WSGIApplication([('/favicon.ico', MainPage)],
                              debug=False)
