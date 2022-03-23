from django.contrib import admin
from django.urls import include, path
from .views import CreateActivity,DeleteActivity
from Activity import views


urlpatterns = [

    path('add/',CreateActivity.as_view()),  
    path('<pk>/delete/',DeleteActivity.as_view()),

]