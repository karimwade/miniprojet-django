from django.shortcuts import render
from .models import Student
# Create your views here.
def index(request):
    return render(request,"index.html")

#about view
def about(request):
    return render(request,"about.html")

#insert data view
def inserData(request):
    if request.method == "POST":
        name=request.POST.get("name")
        mail=request.POST.get("mail")
        gender=request.POST.get("gender")
        print(name,mail,gender)
        #query=Student(name=name)
    return render(request,"index.html")