import re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

def home(response):
    return render(response,"main/home.html", {})

def GetAList(response, id):
    ls = ToDoList.objects.get(id=id)
    my_dict = {
        "ls":ls
    }
    print(my_dict["ls"].item_set.all())
    #items = ls.item_set.get(id=1)
    #return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" % (ls.name, items.text))
    return render(response,"main/list.html", my_dict)

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
    return render(response,"main/create.html", {"form":form})
