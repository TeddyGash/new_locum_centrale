import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render  # get_object_or_404
from django.urls import reverse
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
    @method_decorator(login_required(login_url=LOGIN_URL))
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

    def post(self, request):
        form = LocumForm(request.POST)
        locums = Locum.objects.filter(is_available=True)
        teleconsults = Teleconsults.objects.filter(is_available=True)
        if form.is_valid():
            locum = form.save(commit=False)
            locum.posted_by = request.user
            locum.save()

            # Send Telegram message
            bot_token = "6318375842:AAEqij6jGjqJ7-tA8kZr6aV9pVbPdsk2LYM"
            chat_id = "-975701280"
            api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            link = request.build_absolute_uri(reverse("slots:locums"))
            message = f"New locum posted: [{locum}]({link})"
            payload = {"chat_id": chat_id, "text": message, "parse_mode": "MarkdownV2"}
            response = requests.post(api_url, json=payload)

            if response.status_code == 200:
                # Message sent successfully
                return redirect("/slots/locums")  # Redirect to a success page or locum list view
            else:
                # Failed to send message
                # Handle the error or display an appropriate message to the user
                print("=======message not sent=============")

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
    @method_decorator(login_required(login_url=LOGIN_URL))
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
