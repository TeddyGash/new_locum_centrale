from django.urls import path

from .verify import VerifyMDCDetailsView
from .views import user_detail_view, user_redirect_view, user_update_view

app_name = "users"
urlpatterns = [
    path("verify-mdc-details/", VerifyMDCDetailsView.as_view(), name="verify_mdc_details"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
