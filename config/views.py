from django.shortcuts import render

from newlocumcentrale.slots.models import Locum, Teleconsults


def index(request):
    locums = Locum.objects.filter(is_available=True)
    teleconsults = Teleconsults.objects.filter(is_available=True)
    return render(
        request,
        "index.html",
        {
            "locums": locums,
            "teleconsults": teleconsults,
        },
    )
