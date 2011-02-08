from django.db import models
from datetime import datetime

class Link(models.Model):
    key = models.CharField(max_length = 20)
    longUrl = models.CharField(max_length = 500)
    date = models.DateField(default = datetime.today())

    class Meta:
	db_table = 'link'

    def __unicode__(self):
        return self.key

class Logger(models.Model):
    link = models.ForeignKey(Link)
    date = models.DateField(default = datetime.today())

    class Meta:
	db_table = 'logger'

    def __unicode__(self):
	return self.key 
