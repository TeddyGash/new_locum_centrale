from django.db import models

from config.settings.base import AUTH_USER_MODEL

# from django.contrib.auth.models import User


# Create your models here.


class Locum(models.Model):
    facility = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    shift_starts = models.DateTimeField()
    shift_ends = models.DateTimeField()
    rate_per_shift = models.FloatField()
    contact = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    additional_info = models.TextField(blank=True, null=True)
    posted_by = models.ForeignKey(AUTH_USER_MODEL, related_name="locums", on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("posted_at",)
        verbose_name_plural = "Locum slots"

    def __str__(self):
        return self.facility


class Teleconsults(models.Model):
    date = models.DateTimeField()
    duration = models.CharField(max_length=255)
    communication_medium = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    additional_info = models.TextField(blank=True, null=True)
    posted_by = models.ForeignKey(AUTH_USER_MODEL, related_name="teleconsults", on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("posted_at",)
        verbose_name_plural = "Teleconsults"

    def __str__(self):
        return self.contact
