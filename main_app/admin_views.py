from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main_app.forms import WorkerRegistration, EmployerRegistration
from main_app.models import Worker, Employer, Openings, Request, Feedback, Employer_feed

@login_required(login_url='login_view')
def admin_base(request):
    return render(request,"admin/admin_base.html")

@login_required(login_url='login_view')
def worker_view(request):
    data=Worker.objects.all()
    return render(request,"admin/worker_view.html",{'data':data})


@login_required(login_url='login_view')
def remove(request,id):
    data=Worker.objects.get(id=id)
    data.delete()
    return redirect("worker_view")

@login_required(login_url='login_view')
def update1(request, id):
    data = Worker.objects.get(id=id)
    form = WorkerRegistration(instance=data)
    if request.method == "POST":
        work1 = WorkerRegistration(request.POST, instance=data)
        if work1.is_valid():
            work1.save()
        return redirect("worker_view")
    return render(request, "admin/update_worker.html", {"form": form})




@login_required(login_url='login_view')
def employer_view(request):
    data=Employer.objects.all()
    return render(request,"admin/employer_view.html",{'data':data})

@login_required(login_url='login_view')
def remove2(request,id):
    data=Employer.objects.get(id=id)
    data.delete()
    return redirect("employer_view")

@login_required(login_url='login_view')
def update2(request, id):
    data = Employer.objects.get(id=id)
    form = EmployerRegistration(instance=data)
    if request.method == "POST":
        work2 = EmployerRegistration(request.POST, instance=data)
        if work2.is_valid():
            work2.save()
        return redirect("employer_view")
    return render(request, "admin/update_employer.html", {"form": form})


@login_required(login_url='login_view')
def openings_view(request):
    data = Openings.objects.all()
    return render(request, "admin/openings_view.html", {'data': data})


@login_required(login_url='login_view')
def req_view(request):
    data2=Request.objects.filter(status=1)
    return render(request, "admin/request_view.html", {'data': data2})


@login_required(login_url='login_view')
def accept(request,id):
    obj=Request.objects.get(id=id)
    obj.status = 2
    obj.save()
    return redirect('req_view')


@login_required(login_url='login_view')
def reject(request,id):
    obj=Request.objects.get(id=id)
    obj.status = 0
    obj.save()
    return redirect('req_view')


@login_required(login_url='login_view')
def accept_view(request):
    data=Request.objects.filter(status=2)
    return render(request,"admin/accept.html",{"data":data})



@login_required(login_url='login_view')
def feedback_view(request):
    data=Feedback.objects.all()
    return render(request,"admin/feedback_view.html",{"data":data})



@login_required(login_url='login_view')
def reply_feedback(request,id):
    feedback=Feedback.objects.get(id=id)
    if request.method == "POST":
        r=request.POST.get('reply')
        feedback.reply=r
        feedback.save()
        # messages.info(request,'Reply send')

        return redirect('feedback_view')
    return render(request,"admin/reply_feed.html",{"feedback":feedback})



@login_required(login_url='login_view')
def feedback_employer(request):
    data=Employer_feed.objects.all()
    return render(request,"admin/emp_feed_view.html",{"data":data})



@login_required(login_url='login_view')
def reply_feed_emp(request,id):
    feedback=Employer_feed.objects.get(id=id)
    if request.method == "POST":
        r=request.POST.get('reply_emp')
        feedback.reply=r
        feedback.save()
        # messages.info(request,'Reply send')

        return redirect('feedback_employer')
    return render(request,"admin/reply_emp_feed.html",{"feedback":feedback})








def logou(request):
    logout(request)
    return redirect("/")

