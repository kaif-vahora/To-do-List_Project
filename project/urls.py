from django.contrib import admin
from django.urls import include,path
from project import views

urlpatterns = [
    
    path('addproject/', views.addproject),
    path('viewproject/', views.viewproject),
    path('projectpage/', views.projectpage),

    
]
