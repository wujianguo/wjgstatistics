#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import db
import datetime
class Statistics(db.Model):
	uid = db.StringProperty()
	url = db.StringProperty()
	mtime = db.DateTimeProperty(default=datetime.datetime.utcnow())
	user_agent = db.TextProperty()
	addr = db.TextProperty(default = '')
	ip = db.StringProperty()
