from google.appengine.ext import db
import datetime
class Statistics(db.Model):
	uid = db.StringProperty()
	url = db.StringListProperty()
	mtime = db.ListProperty(item_type=datetime.datetime)
	ip = db.StringListProperty()
