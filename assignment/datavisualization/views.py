from django.shortcuts import render
from django.views.generic import ListView
from .models import MyModel


class MyModelListView(ListView):
    model = MyModel
    template_name = 'assignment\datavisualization\templates\mymodel_list.html'
    context_object_name = 'MyModels'
    print(MyModel.objects.all)
