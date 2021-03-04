from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('loginuser', views.loginuser),
    path('createuser', views.createuser),
    path('success', views.success),
    path('logout', views.logout)
]