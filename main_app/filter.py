import django_filters
from django import forms
from django_filters import CharFilter

from main_app.models import Request


class Job_categoryFilter(django_filters.FilterSet):
    blood=CharFilter(label="",lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder':'search Job_category','class':'form-control'}))

    class Meta:
        model=Request
        fields=("Job_category",)