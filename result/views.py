from django.shortcuts import render
from .models import Result

def home(request):
    results = Result.objects.all()
    return render(request, 'home.html', {'results': results})