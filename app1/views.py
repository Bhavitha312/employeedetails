from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import empform

# Create your views here.
def show(req):
    if req.method=='POST':
        res=empform(req.POST)
        res.save()
        return HttpResponse('data added')
    form=empform()
    return render(req,'index.html',{'form':form})
