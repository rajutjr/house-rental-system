
from django.shortcuts import render,redirect
from django.contrib import messages
#from .models import MILL,adminhouses,adminhouses2,adminhouses3,excel,hello
from .models import *
from django.contrib.auth.models import User,auth
from .form import destform

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

#Home Page before login
def start(request):
    interface1=adminhouses.objects.all()
    interface2=adminhouses2.objects.all()
    interface3=adminhouses3.objects.all()
    value=hello.objects.all()
    #return render(request,'hello.html',{'v':value})
    return render(request,'start.html',{'interface1':interface1,'interface2':interface2,'interface3':interface3})

# first page after login

@login_required(login_url='login')
def page1(request):
    interface1=adminhouses.objects.all()
    interface2=adminhouses2.objects.all()
    interface3=adminhouses3.objects.all()
    return render(request,'page.html',{'interface1':interface1,'interface2':interface2,'interface3':interface3})
# register with an account
def projectregister(request):
    if request.method=='POST':
        first=request.POST['firstname']
        last=request.POST['lastname']
        user=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=user).exists():
                messages.info(request,"username already taken")
                return redirect("projectregister")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect("projectregister")
            else:        
                user=User.objects.create_user(username=user,first_name=first,last_name=last,password=password1,email=email)
                user.save();  
                print("user successfully created")
                return redirect('login')
    else:    
        return render(request,"projectregister.html")

#login with a created account
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            
            interface1=adminhouses.objects.all()
            interface2=adminhouses2.objects.all()
            interface3=adminhouses3.objects.all()
            return render(request,'page.html',{'interface1':interface1,'interface2':interface2,'interface3':interface3})
            #return render(request,"page.html")
        else:
            messages.info(request,"invalid Details")
            return redirect('login')    

    else:    
        return render(request,'projectlogin.html')





#uploading House Details
################################################
@login_required(login_url='login')
def register(request):
    if request.method=='POST':
       form=destform(data=request.POST,files=request.FILES)
       if form.is_valid():
            form.save()
            obj=form.instance
            print("%%%%%%%%%%%%%%%    ",obj,"     %%%%%%%%%%%%%%%%%%%%%%"    )
            return render(request,"page.html",{"obj":obj})  
    else: 
        form=destform()
        dests=MILL.objects.all()
    return render(request,"uploading.html",{"form":form})    




#quering the house details
################################################
@login_required(login_url='login')
def uploaded(request):
    
    dests=MILL.objects.all()
    if request.method=="GET":
        state=request.GET.get("district")
        price=request.GET.get("price")
        area=request.GET.get("area")
        if state!=None and price!=None and area!=None:
            
                dests=MILL.objects.filter(STATE=state,COST__lt=price,CHOOSE_TYPE=area)
                a=MILL.objects.all()
                print("the lenght",len(a))
                
            
    return render(request,'page2.html',{"dests":dests}) 


# detail info about the house
##################################################


@login_required(login_url='login')
def details(request):
    price=request.GET.get("price")
    dests=MILL.objects.all()
    return render(request,'project3.html',{"dests":dests})
def excelsheet(request):
    excelall=excel.objects.all()
    return render(request,'excel.html',{"excelall":excelall})

# admin page customization
def my_view(request):
        print("helloworld")
        return render(request,'start.html')
def ready(request):
    print("second stage")
    return render(request,'excel.html')


@login_required(login_url='login')
def logoutUser(request):
    
    logout(request)
    return redirect('login')
