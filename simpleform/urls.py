from django.contrib import admin
from django.urls import include, path
from .views import CreateAddress
urlpatterns = [
     path('form/',CreateAddress.as_view(),name="adress_form")
]