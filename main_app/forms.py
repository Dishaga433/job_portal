from django import forms
from django.contrib.auth.forms import UserCreationForm

from main_app.models import Login, Worker, Employer, Openings, Request, Feedback, Employer_feed


class LoginRegister(UserCreationForm):
    username=forms.CharField()
    password=forms.CharField(label="password",widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ("username","password")


class WorkerRegistration(forms.ModelForm):
    class Meta:
        model = Worker
        fields ="__all__"
        exclude = ("user",)


class EmployerRegistration(forms.ModelForm):
    class Meta:
        model = Employer
        fields ="__all__"
        exclude = ("user",)



class Job_openings(forms.ModelForm):
    class Meta:
        model = Openings
        fields = "__all__"
        exclude = ("Employer_name","status",)



class Job_request(forms.ModelForm):
    class Meta:
        model = Request
        fields = "__all__"
        exclude = ("Employer_name","status","Worker_name")




class Fdbk(forms.ModelForm):
    class Meta:
        model=Feedback
        fields="__all__"
        exclude=("date","reply","Worker_name",)


class Emp_fdbk(forms.ModelForm):
    class Meta:
        model=Employer_feed
        fields="__all__"
        exclude=("date","reply","Employer_name",)




