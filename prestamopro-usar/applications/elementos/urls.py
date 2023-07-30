from django.contrib import admin
from django.urls import path, include
#from .views import ViewElements
from .views import ListOfelements

urlpatterns = [
    #path("inicio/", ViewElements.as_view(), name="inicio" ),
    path("list/", ListOfelements.as_view(), name="listaprestamo" ),
]