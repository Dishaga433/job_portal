from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main_app.forms import Job_openings, Job_request, Fdbk, WorkerRegistration
from main_app.models import Openings, Worker, Request, Feedback

@login_required(login_url='login_view')
def workers_base(request):
    return render(request,"workers/workers_base.html")


@login_required(login_url='login_view')
def openings_list(request):
    data = Openings.objects.all()
    return render(request, "workers/view_openings.html", {'data': data})


@login_required(login_url='login_view')
def worker_req(request):
    data=Job_request()
    user1=request.user
    print(user1)
    rcvr=Worker.objects.get(user=user1)
    print(rcvr.id)
    if request.method == "POST":
        rname = Job_request(request.POST)
        if rname.is_valid():
            obj=rname.save(commit=False)
            obj.Worker_name=rcvr
            obj.save()
    return render(request,"workers/job_request.html",{"form":data})



@login_required(login_url='login_view')
def req_table(request):
    user1 = request.user
    data = Worker.objects.get(user=user1)
    data2=Request.objects.filter(Worker_name=data)
    return render(request, "workers/request_view.html", {'data': data2})



@login_required(login_url='login_view')
def rmv(request, id):   #request delete aakkan
    data = Request.objects.get(id=id)
    data.delete()
    return redirect("req_table")



@login_required(login_url='login_view')
def feedbk(request):
    data = Fdbk()
    user1=request.user
    rcvr = Worker.objects.get(user=user1)

    if request.method == "POST":
        rname = Fdbk(request.POST)
        if rname.is_valid():
            obj = rname.save(commit=False)
            obj.Worker_name= rcvr
            obj.save()

    return render(request,"workers/feedback.html",{"data":data})



@login_required(login_url='login_view')
def reply(request):
    user1=request.user
    data=Worker.objects.get(user=user1)
    obj=Feedback.objects.filter(Worker_name=data)
    return render(request,"workers/reply.html",{"data":obj})




@login_required(login_url='login_view')
def profile_worker(request):
    user1 = request.user
    data = Worker.objects.get(user=user1)
    return render(request,"workers/worker_profile.html",{"form":data})


@login_required(login_url='login_view')
def worker_update(request, id):
    data = Worker.objects.get(id=id)
    form = WorkerRegistration(instance=data)
    if request.method == "POST":
        profile = WorkerRegistration(request.POST,request.FILES, instance=data)
        if profile.is_valid():
            profile.save()
        return redirect("profile_worker")
    return render(request, "workers/profile_update.html", {"form": form})



def logou(request):
    logout(request)
    return redirect("/")





