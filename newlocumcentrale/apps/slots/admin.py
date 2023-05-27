from django.contrib import admin

from .models import Locum, Teleconsults

# Register your models here.


admin.site.register(Locum)
admin.site.register(Teleconsults)
