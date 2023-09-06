# myapp/urls.py
from django.urls import path
from .views import MyModelListView

urlpatterns = [
    path('mymodels/', MyModelListView.as_view(template_name='html/mymodel_list.html'), name='mymodel_list'),
    # Add more URL patterns as needed
]
