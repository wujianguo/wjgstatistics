#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from google.appengine.api import users
import json
import logging
import datetime
from statistics import Statistics
import jinja2
import os
import urllib
from google.appengine.api import urlfetch

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))


class MainPage(webapp2.RequestHandler):

    def get(self):
        template_values = {'url': None}
        template = JINJA_ENVIRONMENT.get_template('geturl.html')
        self.response.write(template.render(template_values))

    def post(self):
        template_values = {'url': None}
        if True:
            long_url = 's.wujianguo.org/?' + self.request.get(
                'id') + '&' + self.request.get('url')
            params = {'url': long_url}
            params = urllib.urlencode(params)
            result = urlfetch.fetch(url='http://dwz.wujianguo.org/api',
                                    payload=params,
                                    method=urlfetch.POST)
            logging.info(result)
            res = json.loads(result.content)
            logging.info(res)
            template_values=res
        # except Exception as e:
            # logging.error(e)
        logging.info(template_values)
        template = JINJA_ENVIRONMENT.get_template('geturl.html')
        self.response.write(template.render(template_values))
app = webapp2.WSGIApplication([('/geturl', MainPage)],
                              debug=True)
