from django.urls import path

from .views import LocumView, TeleconsultView

app_name = "slots"

urlpatterns = [
    path("locums", LocumView.as_view(), name="locums"),
    path("teleconsults", TeleconsultView.as_view(), name="teleconsults"),
]
