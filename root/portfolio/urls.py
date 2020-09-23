from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('1', views.p1),
    path('2', views.p2),
    path('3', views.p3),
    path('eng', views.eng),
    path('1en', views.e1),
    path('2en', views.e2),
    path('3en', views.e3),

]
