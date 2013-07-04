from google.appengine.ext import db
import datetime


class Statistics(db.Model):
    uid = db.StringProperty()
    url = db.StringProperty()
    mtime = db.DateTimeProperty(default=datetime.datetime.utcnow())
    ip = db.StringProperty()
