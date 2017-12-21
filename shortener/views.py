from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

#function base VIEW
def kirr_redirect_view(req,*args,**kwargs):
    return HttpResponse("hello  from  fucntion ")

#class base VIEW 

class kirrCBirect(View):
    def get(self,req,*args,**kwargs):
        return HttpResponse ("hello from Class view ")
