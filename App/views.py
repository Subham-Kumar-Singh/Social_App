from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'App/home.html')

def loginPage(request):
    return render(request,'App/login.html')

def registerPage(request):
    return render(request,'App/register.html')