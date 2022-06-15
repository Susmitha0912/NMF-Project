from django.shortcuts import render

# Create your views here.
def home(request):
    d={
        'title':'home',
    }
    return render(request,'home.html',d)

def about(request):
    d={
        'title':'about',
    }
    return render(request,'about.html',d)

def founders(request):
    return render(request,'founders.html')
def theme(request):
    return render(request,'theme.html')
def developers(request):
    return render(request,'developers.html')

def Health_Awareness(request):
    d = {
        'title':"health_awareness",
    }
    return render(request,"health_awareness.html",d)

def Menstrual_Hygiene(request):
    return render(request,"menstrual_hygiene.html")

def Education(request):
    return render(request,"education.html")

def login(request):
    return render(request,'login.html')
    