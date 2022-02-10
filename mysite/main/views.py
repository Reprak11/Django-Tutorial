import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def home(response):
    return render(response,"main/home.html", {})

def GetAList(response, id):
    ls = ToDoList.objects.get(id=id)
    my_dict = {
        "ls":ls
    }
    #items = ls.item_set.get(id=1)
    #return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" % (ls.name, items.text))
    return render(response,"main/list.html", my_dict)
