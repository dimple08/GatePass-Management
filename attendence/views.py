from django.shortcuts import redirect, render
from .models import attendence as attendance
from college.models import college as colleges
import datetime

# Create your views here.
def attend(request):
    return render(request, "attendence/attendence.html")

def detail(request):
    if(request.method=="POST"):
        rollno=request.POST.get('xroll')
        data=colleges.objects.filter(rollno=rollno).first()
        c=attendance.objects.filter(rollno=rollno).filter(intime__contains=datetime.date.today()).count()
        if(c>=1):
            data1={"mess":"your attendence is marked"}
            return render(request, "attendence/attendence.html",{"data":data1})
        else:
            att= attendance(date=datetime.date.today(),intime=datetime.datetime.now(),user_id=data.id,rollno=data.rollno)
            att.save()
    return render(request,"attendence/detail.html",{"mydata":data,"Date":datetime.date.today(),"time":datetime.datetime.now()})
        
def attend2(request):
    return render(request, "attendence/attendance2.html")

def detail2(request):
    if(request.method=="POST"):
        rollno=request.POST.get('xroll')
        data=colleges.objects.filter(rollno=rollno).first()
        attn=attendance.objects.filter(rollno=rollno).filter(intime__contains=datetime.date.today()).get()
        attn.outtime=datetime.datetime.now()
        attn.save()
    return render(request,"attendence/detail2.html",{"mydata":data,"Date":datetime.date.today(),"time":datetime.datetime.now()})

def allstudent(request):
    dt=colleges.objects.all()
    return render(request, 'attendence/allstudent.html',{'data':dt})

def edit(request,id):
	bt=colleges.objects.filter(id=id).first()
	return render(request, "attendence/edit.html" ,{"data":bt})

def edit2(request):
    if(request.method=="POST"):
        idd=request.POST.get('xid')
        username=request.POST.get('xname')
        rollno=request.POST.get('xroll')
        email=request.POST.get('xmail')
        mobile=request.POST.get('xmob')
        dp=colleges.objects.get(id=idd)
        dp.username=username
        dp.rollno=rollno
        dp.email=email
        dp.mobile=mobile
        dp.save()
    return redirect('/attendence/allstudent')

def deldata(request,id):
	colleges.objects.filter(id=id).delete()
	return redirect("/attendence/allstudent")

def info(request,id):
    data1=colleges.objects.filter(id=id).first()
    return render(request, 'attendence/info.html', {'data':data1})