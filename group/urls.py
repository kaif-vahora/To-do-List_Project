from django.urls import include, path
from group import views

urlpatterns = [
    path('add/',views.group),
    path('contactUs/',views.contactUS),
    path('aboutUs/',views.aboutUS),
    path('',views.index),

]    