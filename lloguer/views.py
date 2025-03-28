from django.shortcuts import render

# Create your views here.


from .models import Automobil

def llistar_automobils(request):
    automobils = Automobil.objects.all()
    return render(request, 'automobils/llista_automobils.html', {'automobils': automobils})
