from django.shortcuts import render,redirect
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
        return redirect("/")
    return render(request,"index.html",context)

#update view
def updateData(request,id):
    if request.method=="POST":
        name=request.POST["name"]
        mail=request.POST["mail"]
        gender=request.POST["gender"]
        dedit=Student.objects.get(id=id)
        dedit.name=name
        dedit.mail=mail
        dedit.gender=gender
        dedit.save()
        return redirect("/")
    #Recupere l'id du donnée à modifier
    d=Student.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)


#delete view
def deleteData(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    # context={"data":data}
    return redirect("/")