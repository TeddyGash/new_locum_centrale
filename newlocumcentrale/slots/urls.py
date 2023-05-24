from django.urls import path

from newlocumcentrale.slots import views

app_name = "slots"
urlpatterns = [path("locums", views.locum, name="locum"), path("teleconsults", views.teleconsult, name="teleconsult")]
