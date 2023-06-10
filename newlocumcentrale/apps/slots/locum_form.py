from django import forms

from .models import Locum


class LocumForm(forms.ModelForm):
    class Meta:
        model = Locum
        fields = ["facility", "location", "shift_starts", "shift_ends", "rate_per_shift", "contact", "additional_info"]
        widgets = {
            "shift_starts": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "shift_ends": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
