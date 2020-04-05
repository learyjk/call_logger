from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('add', views.add, name='add'),
    path('remove/<int:call_id>/', views.remove, name='remove'),
]
