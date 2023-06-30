from django.contrib.auth.models import AbstractUser
from django.db import models

# from django.db.models import CharField
# from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# class User(AbstractUser):
#     """
#     Default custom user model for newLocumCentrale.
#     If adding fields that need to be filled at user signup,
#     check forms.SignupForm and forms.SocialSignupForms accordingly.
#     """

#     # First and last name do not cover name patterns around the globe
#     name = CharField(_("Name of User"), blank=True, max_length=255)
#     first_name = None  # type: ignore
#     last_name = None  # type: ignore

#     def get_absolute_url(self) -> str:
#         """Get URL for user's detail view.

#         Returns:
#             str: URL for user detail.

#         """
#         return reverse("users:detail", kwargs={"username": self.username})


class User(AbstractUser):
    first_name = models.CharField(max_length=30, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=30, verbose_name=_("Last Name"))
    register_as = models.CharField(
        max_length=30,
        choices=[
            ("doctor", _("Doctor")),
            ("pa", _("Physician Assistant")),
            ("patient", _("Patient")),
            ("employer", _("Employer")),
        ],
        verbose_name=_("Register as"),
    )
    mdc_registration_no = models.CharField(
        max_length=30,
        verbose_name=_("MDC Registration No."),
        blank=True,
        null=True,
    )
    # retrieved data
    verification_status = models.BooleanField(default=False, verbose_name=_("Verification Status"))
    contact = models.CharField(max_length=30, verbose_name=_("Contact"), null=True)
    register_type = models.CharField(max_length=30, verbose_name=_("Register Type"), null=True)
    category = models.CharField(max_length=30, verbose_name=_("Category"), null=True)
    date_of_provisional_reg = models.DateField(null=True)

    def __str__(self):
        return self.username
