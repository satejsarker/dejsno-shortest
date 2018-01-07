from __future__ import unicode_literals

from django.db import models
from  shortener.models import KirrURL


# Create your models here.

class ClickEventManager(models.Model):
    def create_event(self,Kirrinstance ):
        if isinstance(Kirrinstance,KirrURL):
            obj, create = self.get_or_create(kirr_url=Kirrinstance)
            obj.count +=1
            obj.save()
            return obj.count
        return None
    



class ClickEvent(models.Model):
    kirr_url=models.OneToOneField
    count=models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects=ClickEventManager()


    def __str__(self):
        return "{i}".format(i=self.count)
