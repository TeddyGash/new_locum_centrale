from django.shortcuts import render  # get_object_or_404
from django.views import View

from .models import Locum, Teleconsults


class LocumView(View):
    def get(self, request):
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


class TeleconsultView(View):
    def get(self, request):
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
