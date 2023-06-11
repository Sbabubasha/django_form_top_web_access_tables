from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def topic_insertion(request):
    if request.method=='POST':
        un=request.POST['user']
        to=Topic.objects.get_or_create(topic_name=un)[0]
        to.save()
        return HttpResponse('topic datainsertion is successfull...😊!')
    return render(request,'topic_insertion.html')



def web_insertion(request):
    lot=Topic.objects.all()
    d={'topics':lot}
    if request.method=='POST':
        one=request.POST['topic']
        two=request.POST['n']
        thr=request.POST['u']
        fo=request.POST['e']
        TO=Topic.objects.get_or_create(topic_name=one)[0]
        TO.save()
        WO=Webpage.objects.get_or_create(topic_name=TO,name=two,url=thr,email=fo)[0]
        WO.save()

        return HttpResponse('data insertion is successfull...😊!')
    return render(request,'web_insertion.html',d)
    

def access_insertion(request):
    loa=Webpage.objects.all()
    d={'name':loa}
    if request.method=='POST':
            n=request.POST['name']
            a=request.POST['atr']
            dt=request.POST['date'] 
            wo=Webpage.objects.get(name=n)
            aO=Accessrecords.objects.get_or_create(name=wo,author=a,date=dt)[0]
            aO.save()
            return HttpResponse('Accessrecords data insertion is successfully...😊🤯🥱😴!')
    return render(request,'access_insertion.html',d)


def multiple(request):
    lot=Topic.objects.all()
    d={'topics':lot}
    if request.method=='POST':
        td=request.POST.getlist('multi')
        webqueryset=Webpage.objects.none()
        for i in td:
            webqueryset=webqueryset|Webpage.objects.filter(topic_name=i)
        d1={'webpages':webqueryset}
        return render(request,'display_webpage.html',d1)
    return render(request,'multiple.html',d)