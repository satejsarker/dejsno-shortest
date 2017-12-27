from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from shortener.models import KirrURL
from .forms import SubmitUrlForm

#function base VIEW

class HomeView(View):
    def get(self,req,*args,**kwargs):
        forms=SubmitUrlForm()
        contex={
            "title":"submit URL",
            "form":forms
        }
        return render(req, "shortener/home.html", contex)

    def post(self, req, *args, **kwargs):
       
        forms=SubmitUrlForm(req.POST)
        contex = {
            "title": "submit URL",
            "form": forms
        }
        template = "shortener/home.html"
        if forms.is_valid():
            print(forms.cleaned_data.get('url'))
            new_url=forms.cleaned_data.get('url')
            obj,created=KirrURL.objects.get_or_create(url=new_url)
            context={
                "object":obj,
                "created":created
            }
            if created:
                template = "shortener/sucess.html"
            else:
                template = "shortener/already-created.html"
        
                template = "shortener/already-created.html"
        return render(req,  template, context)

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
