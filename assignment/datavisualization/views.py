from django.shortcuts import render
from django.views.generic import ListView
from .models import MyModel


class MyModelListView(ListView):
    model = MyModel
    template_name = 'html\mymodel_list.html'
    context_object_name = 'MyModel'
    