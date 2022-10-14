from django.shortcuts import render,redirect
from .models import college as colleges
from django.core.files.storage import FileSystemStorage

# Create your views here.

def dashboard(request):
    return render(request, "college/dashboard.html")
def adminlogin(request):
    if(request.method=="POST"):
        username=request.POST.get('xuser')
        password=request.POST.get('xpass')
        if(username=="admin" and password=="admin"):
            return render(request, "college/dashboard.html")
        else:
            return render(request, "admin1/login.html")

def student(request):
    return render(request, "college/student.html")

def studentreg(request):
    if(request.method=="POST"):
        username=request.POST.get('xname')
        rollno=request.POST.get('xroll')
        email=request.POST.get('xmail')
        mobile=request.POST.get('xmob')
        image=request.FILES['xfile']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)   
        c=colleges(username=username,rollno=rollno, email=email, mobile=mobile, image=image.name)
        c.save()
        data={"mess":"Successfully insert data","status":True}
        return render(request, "college/student.html",{"mydata":data})
    else:
        return redirect("/college/")
    