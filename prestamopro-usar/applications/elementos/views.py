from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Prestamo


# Create your views here.
#class ViewElements(TemplateView):
#    template_name="elementos/index.html"

class ListOfelements(ListView):
    model=Prestamo
    template_name="elementos/index.html"
    context_object_name="listaprestamos"
   
