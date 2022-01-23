from unicodedata import name
from . import views
from django.urls import path 

urlpatterns = [
    path('',views.main,name="home"),
    path('login/', views.login,name="login"),
    path('car/', views.chooseCar,name="car"),
    path('cslidecarsar/', views.slidecars,name="slidecars"),
]
