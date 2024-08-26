from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic created successfully')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        url=request.POST['url']
        email=request.POST['email']

        RTO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=RTO,name=na,url=url,email=email)[0]
        WO.save()
        return HttpResponse('webpage created successfully')
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    if request.method=='POST':
        na=request.POST['na']
        d=request.POST['d']
        au=request.POST['au']

        RWO=Webpage.objects.get(id=na)
        AO=AccessRecord.objects.get_or_create(name=RWO,date=d,author=au)[0]
        AO.save()
        return HttpResponse('Access record created successfully')
    return render(request,'insert_access.html',d) 


def select_multiple(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}

    if request.method=='POST':
        STL=request.POST.getlist('tn')
        WOS=Webpage.objects.none()
        for t in STL:
            WOS=WOS|Webpage.objects.filter(topic_name=t)
        d1={'WOS':WOS}
        return render(request,'display_webpage.html',d1)
    return render(request,'select_multiple.html',d)



def checkbox(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}

    return render(request,'checkbox.html',d)