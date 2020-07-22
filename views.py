from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from . import models
# Create your views here.
from . import forms
def insertpage(request):
    f1=forms.MyForm()
    return render(request,"insert.html",{'form':f1})

def getdata(request):
    if request.method=='GET':
        un=request.GET['Username']
        p=request.GET['Password']
        Ph=request.GET['PhoneNo']
        Ad=request.GET['Address']

        return render(request,"valid.html",{"username":un,"password":p,"phoneno":Ph,"address":Ad})
    if request.method=='POST':
        un=request.POST['Username']
        p=request.POST['Password']
        Ph=request.POST['PhoneNo']
        Ad=request.POST['Address']
        c1=models.Customer(Username=un,Password=p,PhoneNo=Ph,Address=Ad)
        c1.save()

        return render(request,"valid.html",{"Username":un,"Password":p,"phoneno":Ph,"address":Ad})