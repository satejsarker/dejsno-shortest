from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from shortener.models import KirrURL

#function base VIEW

class HomeView(View):
    def get(self,req,*args,**kwargs):
        return render(req, "shortener/home.html", {})

    def post(self, req, *args, **kwargs):
        print(req.POST)
        print(req.POST.get('url'))
        return render(req, "shortener/home.html", {})

def kirr_redirect_view(req, shortcode=None, *args,  **kwargs):
    
    # print (args)
    # print(kwargs)
    # obj=KirrURL.objects.get(shortcode=shortcode)
    # try:
    #     obj = KirrURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = KirrURL.objects.get(shortcode='asdsd')
    # obj = get_object_or_404(KirrURL, shortcode=shortcode)
    # obj_url=obj
    obj_url=None
   
    qs=KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
    if qs.exists() and qs.count() ==1:
        obj=qs.first()
        obj_url=obj.url
    return HttpResponseRedirect(obj_url)

#class base VIEW 

class kirrCBirect(View):
    def get(self, req, shortcode=None, *args,  **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponse ("hello from Class view {sc}".format(sc=shortcode))
    def post(self,req,*args,**kwargs):
        return HttpResponse()
