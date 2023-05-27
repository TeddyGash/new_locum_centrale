from django.shortcuts import render
from django.views import View

from newlocumcentrale.apps.slots.models import Locum, Teleconsults


class HomePageView(View):
    def get(self, request):
        locums = Locum.objects.filter(is_available=True)
        teleconsults = Teleconsults.objects.filter(is_available=True)
        # return render(request, "home.html")
        return render(
            request,
            "home.html",
            {
                "locums": locums,
                "teleconsults": teleconsults,
            },
        )
