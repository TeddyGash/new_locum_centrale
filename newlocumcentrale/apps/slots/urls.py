from django.urls import path

from .views import LocumCreateView, LocumView, TeleconsultCreateView, TeleconsultView

app_name = "slots"

urlpatterns = [
    path("locums", LocumView.as_view(), name="locums"),
    path("teleconsults", TeleconsultView.as_view(), name="teleconsults"),
    path("post_locum/", LocumCreateView.as_view(), name="post_locum"),
    path("post_teleconsult/", TeleconsultCreateView.as_view(), name="post_teleconsult"),
]
