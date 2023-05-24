from django.shortcuts import render

from .models import Locum, Teleconsults

# Create your views here.


def locum(request):
    locums = Locum.objects.filter(is_available=True)
    teleconsults = Teleconsults.objects.filter(is_available=True)
    return render(
        request,
        "slots/locums.html",
        {
            "locums": locums,
            "teleconsults": teleconsults,
        },
    )


def teleconsult(request):
    locums = Locum.objects.filter(is_available=True)
    teleconsults = Teleconsults.objects.filter(is_available=True)
    return render(
        request,
        "slots/teleconsults.html",
        {
            "locums": locums,
            "teleconsults": teleconsults,
        },
    )
