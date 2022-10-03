from django.shortcuts import render

# Create your views here.
def uno(request):
    return render(request,"home.html")

def dos(request):
    return render(request,"dos.html")