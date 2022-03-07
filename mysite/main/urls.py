from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("<int:id>", views.GetAList,name="GetAList"),
    path("create/", views.create,name="create")
]