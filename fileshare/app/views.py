from django.core.files.base import File
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import *


def loginuser(request):
   
    if request.method=='POST':

        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)
        if user is None:
            return redirect(loginuser)
        else:
            login(request,user)
            return redirect(index)
    return render(request,'login.html')

@login_required(login_url='/login/')
def logoutuser(request):
    logout(request)
    return redirect(loginuser)

@login_required(login_url='/login/')
def index(request):
    files=Files.objects.filter(user_id=request.user.id)
    sharedfiles=Shared.objects.filter(shared_id=request.user.id)
    data={
        "data":files,
        "shared":sharedfiles
    }
    
        
    return render(request,'index.html',data)

@login_required(login_url='/login/')
def add(request):
    
    if request.method=='POST':

        name=request.POST['name']
        desc=request.POST['description']
        file=request.FILES['file']

        data=Files(name=name,description=desc,file=file,user_id=request.user.id)
        data.save()
       
        return redirect(index)
        
         
        
        return redirect(index)
    return render(request,'add.html')

@login_required(login_url='/login/')
def read(request,id):
    file=Files.objects.get(id=id,user_id=request.user.id)
    comments=Comments.objects.filter(file_id=id)
    users=User.objects.all()
    
    return render(request,'read.html',{'data':file,'comments':comments,'user':users})
    
@login_required(login_url='/login/')
def deletefile(request,id):
    file=Files.objects.get(id=id,user_id=request.user.id)
    import os
    os.remove(f"{file.file}")
    file.delete()
    
    return redirect(index)
    
@login_required(login_url='/login/')
def update(request,id):
    file=Files.objects.get(id=id,user_id=request.user.id)
    if request.method=='POST':
       import os
       os.remove(f"{file.file}")
       file.name=request.POST['name']
       file.description=request.POST['description']
       file.file=request.FILES['file']

       file.save()
       

    
    
    return render(request,'update.html',{"data":file})
    
@login_required(login_url='/login/')
def addcomment(request,id):
    
    if request.method=='POST':
       
       data=Comments(user_id=request.user.id,file_id=id,comment=request.POST['comment'])
       data.save()
       return redirect(read,id)
       

    
    
    return redirect(read,id)

@login_required(login_url='/login/')
def deletecomment(request,id,postid):
    
    data=Comments.objects.get(id=id,user_id=request.user.id).delete()
    
    
    return redirect(read,postid)

@login_required(login_url='/login/')
def share(request,fileid):

    data={
        "user":User.objects.filter(~Q(id=request.user.id)),
        "fileid":fileid
    }
    if request.method=='POST':
        data=Shared(owner_id=request.user.id,shared_id=request.POST['user'],file_id=fileid)
        data.save()
        return redirect(read,fileid)
    


    return render(request,'share.html',data)

@login_required(login_url='/login/')
def readshared(request,user,fileid):

    
    data={
        
        "data":Files.objects.get(id=fileid),
        "comments":Comments.objects.all(),
        "user":User.objects.all()
        
    }

    return render(request,'sharedpost.html',data)

@login_required(login_url='/login/')
def addcommentshared(request,id):
    
    if request.method=='POST':
       
       data=Comments(user_id=request.user.id,file_id=id,comment=request.POST['comment'])
       data.save()
       return redirect(readshared,id)
       

    
    
    return redirect(readshared,id)




    





  