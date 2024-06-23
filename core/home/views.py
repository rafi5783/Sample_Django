from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    peoples=[
        {'name': 'Abhijet','age':35},
        {'name': 'Tambhita','age': 25},
        {'name': 'sandeep','age':24},
        {'name': 'panditha','age':28}
    ]

    vegetable =[
        'tomato',
        'cucumber',
        'okra'
    ]

    for people in peoples:
        print(people)

    return render(request,"home/index.html",context={'peoples':peoples,'vegetable':vegetable})

def about(request):
    return render(request,"home/about.html")

def contact(request):
    return render(request,"home/contact.html")

def success_page(request):
    print("*"*10)
    return HttpResponse("<h1>Hey these is a success page</h1>")