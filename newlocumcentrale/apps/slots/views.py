from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render  # get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View

from config.settings.base import LOGIN_URL

from .forms import LocumForm, TeleconsultForm
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


class LocumCreateView(View):
    def get(self, request):
        form = LocumForm()
        locums = Locum.objects.filter(is_available=True)
        teleconsults = Teleconsults.objects.filter(is_available=True)
        return render(
            request,
            "slots/post_locum.html",
            {
                "form": form,
                "locums": locums,
                "teleconsults": teleconsults,
            },
        )

    @method_decorator(login_required(login_url=LOGIN_URL))
    def post(self, request):
        form = LocumForm(request.POST)
        locums = Locum.objects.filter(is_available=True)
        teleconsults = Teleconsults.objects.filter(is_available=True)
        if form.is_valid():
            locum = form.save(commit=False)
            locum.posted_by = request.user
            locum.save()
            return redirect("/slots/locums")  # Redirect to a success page or locum list view
        return render(
            request,
            "slots/post_locum.html",
            {
                "form": form,
                "locums": locums,
                "teleconsults": teleconsults,
            },
        )


class TeleconsultCreateView(View):
    def get(self, request):
        form = TeleconsultForm()
        locums = Locum.objects.filter(is_available=True)
        teleconsults = Teleconsults.objects.filter(is_available=True)
        return render(
            request,
            "slots/post_teleconsult.html",
            {
                "form": form,
                "locums": locums,
                "teleconsults": teleconsults,
            },
        )

    @method_decorator(login_required(login_url=LOGIN_URL))
    def post(self, request):
        form = TeleconsultForm(request.POST)
        locums = Locum.objects.filter(is_available=True)
        teleconsults = Teleconsults.objects.filter(is_available=True)
        if form.is_valid():
            locum = form.save(commit=False)
            locum.posted_by = request.user
            locum.save()
            return redirect("/slots/teleconsults")  # Redirect to a success page or locum list view
        return render(
            request,
            "slots/post_teleconsult.html",
            {
                "form": form,
                "locums": locums,
                "teleconsults": teleconsults,
            },
        )
