from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('add_call', views.add_call, name='add_call'),
    path('add_callee', views.add_callee, name='add_callee'),
    path('rolodex', views.rolodex, name='rolodex'),
    path('remove_call/<int:call_id>/', views.remove_call, name='remove_call'),
    path('remove_callee/<int:callee_id>/', views.remove_callee, name='remove_callee'),
]
