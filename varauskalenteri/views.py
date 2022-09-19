from importlib.resources import contents
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from .models import Tapahtuma


def tapahtumalistaus(request):
    tapahtumat = Tapahtuma.objects.all()
    context = {
        'tapahtumat': tapahtumat,
    }
    return render(request, 'listaus.html', context)

def varaa_tapahtuma(request, id):
    if request.method == "POST":
        tapahtuma.varaa(request.user)
        context = ["varattu"] = True
    else:
        varattu = tapahtuma.onko_varattu(request.user)
        context["varattu"] = False
    return render(request, "varaa.html", context)