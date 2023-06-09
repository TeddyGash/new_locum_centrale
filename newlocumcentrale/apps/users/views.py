from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

# from django.http import HttpResponse
from django.urls import reverse  # reverse_lazy
from django.utils.translation import gettext_lazy as _

# from django.views import View
from django.views.generic import DetailView, RedirectView, UpdateView

from newlocumcentrale.apps.slots.models import Locum, Teleconsults

# from .verification_script import verify_mdc_details

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "account/user_detail.html"
    # context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        locums = Locum.objects.filter(is_available=True)
        teleconsults = Teleconsults.objects.filter(is_available=True)
        # context["first_name"] = user.first_name
        context["user"] = user
        context["locums"] = locums
        context["teleconsults"] = teleconsults
        return context


# class UserDetailView(LoginRequiredMixin, DetailView):
#     model = User
#     slug_field = "username"
#     slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()

# class UserDetailView(LoginRequiredMixin, DetailView):
#     model = User
#     slug_field = "username"
#     slug_url_kwarg = "username"
#     template_name = "account/user_detail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         locums = Locum.objects.filter(is_available=True)
#         teleconsults = Teleconsults.objects.filter(is_available=True)
#         context["locums"] = locums
#         context["teleconsults"] = teleconsults
#         return context


# # class UserDetailView(LoginRequiredMixin, DetailView):
# #     model = User
# #     slug_field = "username"
# #     slug_url_kwarg = "username"


# user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()

# new view to be implemented
# class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     model = User
#     fields = ["name"]
#     success_message = _("Information successfully updated")
#     template_name = "users/user_update.html"  # Replace with your custom template

#     def get_success_url(self):
#         return reverse_lazy("users:detail", kwargs={"username": self.request.user.username})


# class UserRedirectView(LoginRequiredMixin, RedirectView):
#     permanent = False

#     def get_redirect_url(self):
#         return reverse_lazy("users:detail", kwargs={"username": self.request.user.username})


# class VerifyMDCDetailsView(View):
#     def post(self, request):
#         full_name = f"{request.POST.get('first_name')} {request.POST.get('last_name')}"
#         category = request.POST.get("category")  # Assuming category is passed in the form data
#         mdc_number = request.POST.get("mdc_number")  # Assuming mdc_number is passed in the form data

# result = verify_mdc_details(category, mdc_number, full_name)

# return HttpResponse(result)
