from django.shortcuts import render_to_response
from .models import Line

def home(request):
  return render_to_response("search/home.html",{'lines':Line.objects.all()})
