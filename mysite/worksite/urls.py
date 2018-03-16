from django.urls import path
from django.conf.urls import url
from worksite import views

urlpatterns = [
    path("", views.Index.as_view()),
    path("login", views.login),  
    path("logout", views.logout),  
    path("delete", views.delete),
    path("edit", views.edit),
    path("init", views.init),
    path("search", views.search),
]