from django import forms

from .models import Locum, Teleconsults


class LocumForm(forms.ModelForm):
    class Meta:
        model = Locum
        fields = ["facility", "location", "shift_starts", "shift_ends", "rate_per_shift", "contact", "additional_info"]
        widgets = {
            "shift_starts": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "shift_ends": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class TeleconsultForm(forms.ModelForm):
    class Meta:
        model = Teleconsults
        fields = ["date", "duration", "communication_medium", "contact", "additional_info"]
        widgets = {
            "date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            # "shift_ends": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
