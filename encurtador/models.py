from django.db import models

class Link(models.Model):
    key = models.CharField(max_length = 20)
    longUrl = models.CharField()
    date = models.DateField()

    def __unicode__(self):
        return self.key

class Logger(models.Model):
    link = models.ForeignKey(Link)
    date = models.DateField() 
