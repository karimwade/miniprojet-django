from django.shortcuts import render
from .models import Student
# Create your views here.
def index(request):
    #load data on the template
    data=Student.objects.all()
    context={"data":data}
    return render(request,"index.html",context)

#about view
def about(request):
    return render(request,"about.html")

#insert data view
def inserData(request):
    data=Student.objects.all()
    context={"data":data}
    if request.method == "POST":
        name=request.POST.get("name")
        mail=request.POST.get("mail")
        gender=request.POST.get("gender")
        print(name,mail,gender)
        query=Student(name=name,mail=mail,gender=gender)
        query.save()
    return render(request,"index.html",context)