from __future__ import unicode_literals
from django.conf import settings
from django.db import models
#from django.core.urlresolvers import reverse

from django_hosts.resolvers import reverse
from .util import code_generator,create_shortcode
from .validators import validate_dot_com,validate_url

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX',15)

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
    url=models.CharField(max_length=220,validators=[validate_url,validate_dot_com])
    shortcode=models.CharField(max_length=SHORTCODE_MAX,blank=True,null=True,unique=True)
    updated=models.DateTimeField(auto_now=True,null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    active=models.BooleanField(default=True)

    objects=KirrURLManager()

    
    def save(self,*args,**kwargs):
       if self.shortcode is None or self.shortcode=="":
           self.shortcode = code_generator()
           
       super(KirrURL,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.url)
    def __unicode__(self):
        return str(self.url)
    def get_short_url(self):
        url_path = reverse("scode", kwargs={'shortcode':self.shortcode},host='www',scheme='http',port="8000")
        return url_path
 
