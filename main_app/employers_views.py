from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main_app.filter import Job_categoryFilter
from main_app.forms import Job_openings, EmployerRegistration, Emp_fdbk
from main_app.models import Employer, Openings, Request, Employer_feed

@login_required(login_url='login_view')
def employer_base(request):
    return render(request,"employers/employers_base.html")


@login_required(login_url='login_view')
def add_openings(request):
    data=Job_openings()
    user1=request.user
    print(user1)
    rcvr=Employer.objects.get(user=user1)
    print(rcvr.id)
    if request.method == "POST":
        rname = Job_openings(request.POST)
        if rname.is_valid():
            obj=rname.save(commit=False)
            obj.Employer_name=rcvr
            obj.save()
    return render(request,"employers/add_openings.html",{"form":data})



@login_required(login_url='login_view')
def view_openings(request):
    user1 = request.user
    data = Employer.objects.get(user=user1)
    data2=Openings.objects.filter(Employer_name=data)
    return render(request, "employers/view_openings.html", {'data': data2})



@login_required(login_url='login_view')
def rmv(request, id):
    data = Openings.objects.get(id=id)
    data.delete()
    return redirect("view_openings")



@login_required(login_url='login_view')
def update3(request,id):
    data = Openings.objects.get(id=id)
    print(data)
    form = Job_openings(instance=data)
    print(form)
    if request.method == "POST":
        work2 = Job_openings(request.POST, instance=data)
        if work2.is_valid():
            work2.save()
        return redirect("view_openings")
    return render(request, "employers/openings_update.html", {"form": form})



@login_required(login_url='login_view')
def view_req(request):
    obj=Request.objects.all()
    bloodfilter = Job_categoryFilter(request.GET, queryset=obj)
    data = bloodfilter.qs
    return render(request, "employers/request_view.html", {'data': data,"bloodfilter":bloodfilter})




@login_required(login_url='login_view')
def accept_emp(request,id):
    obj2=Request.objects.get(id=id)
    user1=request.user
    data=Employer.objects.get(user=user1)
    obj2.Employer_name=data
    obj2.status = 1
    obj2.save()
    return redirect("view_req")




@login_required(login_url='login_view')
def feedbk_emp(request):
    data = Emp_fdbk()
    user1=request.user
    rcvr = Employer.objects.get(user=user1)

    if request.method == "POST":
        rname = Emp_fdbk(request.POST)
        if rname.is_valid():
            obj = rname.save(commit=False)
            obj.Employer_name= rcvr
            obj.save()

    return render(request,"employers/feedback.html",{"data":data})



@login_required(login_url='login_view')
def reply_emp(request):
    user1=request.user
    data=Employer.objects.get(user=user1)
    obj=Employer_feed.objects.filter(Employer_name=data)
    return render(request,"employers/reply.html",{"data":obj})




@login_required(login_url='login_view')
def profile_employer(request):
    user1 = request.user
    data = Employer.objects.get(user=user1)
    return render(request,"employers/employer_profile.html",{"form":data})




@login_required(login_url='login_view')
def employer_update(request, id):
    data = Employer.objects.get(id=id)
    form = EmployerRegistration(instance=data)
    if request.method == "POST":
        profile2 = EmployerRegistration(request.POST,request.FILES, instance=data)
        if profile2.is_valid():
            profile2.save()
        return redirect("profile_employer")
    return render(request, "employers/profile_update.html", {"form": form})





def logou(request):
    logout(request)
    return redirect("/")




