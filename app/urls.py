from django.urls import path
from app import views
urlpatterns = [
    path('',views.index,name="index"),
    path('insert',views.inserData,name="insert"),
    path('about',views.about,name="about"),
    path('update/<id>',views.updateData,name="update"),
    path('delete/<id>',views.deleteData,name="delete")

]