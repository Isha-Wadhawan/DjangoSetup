from django.shortcuts import render , HttpResponse

def greet(request):
    return HttpResponse("<h1>Hello, World !</h1>")