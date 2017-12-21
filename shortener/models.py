from __future__ import unicode_literals

from django.db import models
from .util import code_generator,create_shortcode


# Create your models here.
class KirrURLManager(models.Manager):
    def all(self,*args,**kwargs):
        qs_main=super(KirrURLManager,self).all(*args,**kwargs)
        qs=qs_main.filter(active=False)

        return qs
    def refresh_shortcodes(self):
        qs=KirrURL.objects.filter(id__gte=1)
        new_code=0
        for q in qs:
            q.shortcode=create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_code +=1
        return "new codes made :{i}".format(i=new_code)




class KirrURL(models.Model):
    url=models.CharField(max_length=220)
    shortcode=models.CharField(max_length=30,blank=True,null=True,unique=True)
    updated=models.DateTimeField(auto_now=True,null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    active=models.BooleanField(default=True)

    objects=KirrURLManager()

    
    def save(self,*args,**kwargs):
       if self.shortcode is None or self.shortcode=="":
           self.shortcode=create_shortcode(self)
           
       super(KirrURL,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.url)
    def __unicode__(self):
        return str(self.url)
    