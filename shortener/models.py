from __future__ import unicode_literals

from django.db import models

# Create your models here.
class KirrURL(models.Model):
    url=models.CharField(max_length=220)
    shortcode=models.CharField(max_length=30,null=True,unique=True)
    updated=models.DateTimeField(auto_now=True,null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return str(self.url)
    def __unicode__(self):
        return str(self.url)
    