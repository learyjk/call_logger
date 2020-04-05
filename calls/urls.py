from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='add'),
    path('add', views.search, name='search'),
    path('remove', views.search, name='remove'),
]
