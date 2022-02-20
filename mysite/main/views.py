from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
from django.db import IntegrityError
# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/base.html", {})

def v1(response):
    return HttpResponse("<h1> View 1 </h1>")

def display(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == 'POST':
        if response.POST.get('save'):
            for item in ls.item_set.all():
                if response.POST.get('c' + str(item.id)) == 'clicked':
                    item.completed = True
                else:
                    item.completed = False

                item.save()

        elif response.POST.get('new_item'):
            txt = response.POST.get('new')

            if len(txt) > 2:
                ls.item_set.create(text=txt, completed=False)
            else:
                print('Invalid Name for entry!')

    return render(response, "main/display.html", {'ls': ls})

def create(response):
    if response.method == 'POST':
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(name=n)
            try:
                t.save()
                return HttpResponseRedirect(f'/display/{t.id}')
            except IntegrityError:
                print('IntegrityError in Database')

    else:
        form = CreateNewList()
    return render(response, "main/create.html", {'form': form})
