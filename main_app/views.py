from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect

from main_app.forms import LoginRegister, WorkerRegistration, EmployerRegistration


# Create your views here.
def index(request):
    return render(request,"index.html")

def dashboard(request):
    return render(request,"dashboard.html")






def WorkerR(request):
    form1 = LoginRegister()
    form2=WorkerRegistration()

    if request.method=="POST":
        form1 = LoginRegister(request.POST)
        form2=WorkerRegistration(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            user1=form1.save(commit=False)
            user1.is_worker=True
            user1.save()
            user2=form2.save(commit=False)
            user2.user=user1
            user2.save()
            return redirect("login_view")


    return render(request,"worker_registration.html",{"form1":form1,"form2":form2})



def EmployerR(request):
    form1 = LoginRegister()
    form2=EmployerRegistration()

    if request.method=="POST":
        form1 = LoginRegister(request.POST)
        form2=EmployerRegistration(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            user1=form1.save(commit=False)
            user1.is_employer=True
            user1.save()
            user2=form2.save(commit=False)
            user2.user=user1
            user2.save()
            return redirect("login_view")


    return render(request,"employer_registration.html",{"form1":form1,"form2":form2})



def Login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('password')
        print(username)
        print(password)

        user=authenticate(request,username=username,password=password)
        print(user)

        if user is not None:
            login(request,user)
            if user.is_staff:
                print("admin")
                return redirect("admin_base")

            elif user.is_worker:
                print("admin")
                return redirect("workers_base")

            elif user.is_employer:
                print("admin")
                return redirect("employers_base")

        else:
            messages.info(request,'invalid credentials')
    return render(request,"login.html")


