from django.urls import path
from django.conf.urls import url
from demo import views

urlpatterns = [
    path("add", views.add),
    path("sendemail", views.sendemail),
]