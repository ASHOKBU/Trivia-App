from django.shortcuts import render,redirect
from app.models import *
# Create your views here.
def createname(request):
    if request.method=='POST':
        name=request.POST.get('name')
        n=CreateName.objects.get_or_create(name=name)
        if n[1]==True:
            n[0].save()
        return redirect('question1')
    return render(request,"createname.html")
def question1(request):
    if request.method=="POST":
        answer= request.POST.get('answer')
        ans1=Question1.objects.get_or_create(answer1=answer)
        if ans1[1]==True:
            ans1[0].save()
        return redirect('question2')
    return render(request,'question1.html')
def question2(request):
    if request.method=="POST":
        answer= request.POST.getlist('answer')
        ans2=Question2.objects.get_or_create(answer2=answer)
        if ans2[1]==True:
            ans2[0].save()
        return redirect('summary')
    return render(request,'question2.html')
def summary(request):
    name=CreateName.objects.all()
    question1=Question1.objects.all()
    question2=Question2.objects.all()
    return render(request,"summary.html",context={name:'name',question1:'question1',question2:'question2'})
