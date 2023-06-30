from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm

# from django.contrib.auth import forms
from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    # class Meta(forms.UserChangeForm.Meta):
    #     model = User
    pass


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    # class Meta(forms.UserCreationForm.Meta):
    #     model = User
    #     error_messages = {
    #         "username": {"unique": _("This username has already been taken.")},
    #     }
    # pass


# class UserSignupForm(SignupForm):
#     """
#     Form that will be rendered on a user sign up section/screen.
#     Default fields will be added automatically.
#     Check UserSocialSignupForm for accounts created from social.
#     """

# from allauth.account.forms import SignupForm
# from django.utils.translation import gettext_lazy as _


class UserSignupForm(SignupForm):
    print("===================k==k==k=k=k==k=k=k=k=k=k=k=k==k=k=k=k=k==k=")

    first_name = forms.CharField(max_length=30, label=_("First Name"))
    last_name = forms.CharField(max_length=30, label=_("Last Name"))
    username = forms.CharField(max_length=150, label=_("Username"))
    email = forms.EmailField(label=_("Email"))
    register_as = forms.ChoiceField(
        choices=[
            ("Doctor", _("Doctor")),
            ("PA", _("Physician Assistant")),
            ("patient", _("Patient")),
            ("employer", _("Employer")),
        ],
        label=_("Register as:"),
        widget=forms.Select(attrs={"id": "register_as_select"}),
    )

    mdc_registration_no = forms.CharField(
        max_length=30,
        label=_("MDC Registration No.:"),
        required=False,
        widget=forms.TextInput(
            attrs={"id": "mdc_registration_no_input", "placeholder": _("Enter MDC Registration No.")}
        ),
    )
    password1 = forms.CharField(widget=forms.PasswordInput, label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput, label=_("Repeat Password"))
    # mdc_registration_no = forms.CharField(max_length=30, label=_('MDC Registration No.'), required=False)

    print("===================k==k==k=k=k==k=k=k=k=k=k=k=k==k=k=k=k=k==k=", mdc_registration_no)

    # response_data = receive_data()
    # response_data = {}

    class Meta:
        model = User
        exclude = ["verification_status", "contact", "register_type", "date_of_provisional_reg", "category"]

    print(mdc_registration_no)

    def clean(self):
        cleaned_data = super().clean()
        register_as = cleaned_data.get("register_as")
        mdc_registration_no = cleaned_data.get("mdc_registration_no")

        if register_as in ["Doctor", "PA"] and not mdc_registration_no:
            self.add_error(
                "mdc_registration_no", _("MDC Registration No. is required for Doctors and Physician Assistants.")
            )

        return cleaned_data

    # def receive_data(self, response_data):
    #     # self.response_data = response_data
    #     # return self.response_data
    #     self.response_data.update(response_data)

    # def __init__(self, *args, **kwargs):
    #     # response_data = kwargs.pop('response_data', {})
    #     super().__init__(*args, **kwargs)
    #     self.fields["password1"].widget.attrs.update({"autocomplete": "new-password"})
    #     self.fields["password2"].widget.attrs.update({"autocomplete": "new-password"})
    # self.response_data = response_data

    # def save(self, request):
    #     # user = super().save(request)
    #     # response_data = request.session.get('response_data')
    #     # Retrieve the response_data from cache
    #     print("HHHHHHHHHHHHH", self.cleaned_data["mdc_registration_no"], "HHHHHHHHHHHHHHHHHHHHH")
    #     response_data = cache.get(self.cleaned_data["mdc_registration_no"])
    #     print('response_data in save():======================', response_data )
    #     user.first_name = self.cleaned_data["first_name"]
    #     user.last_name = self.cleaned_data["last_name"]
    #     user.username = self.cleaned_data["username"]
    #     user.email = self.cleaned_data["email"]
    #     user.register_as = self.cleaned_data["register_as"]
    #     user.mdc_registration_no = self.cleaned_data["mdc_registration_no"]
    #     user.verification_status = response_data['verification_status']
    #     user.contact = response_data['phone']
    #     user.register_type = response_data['register_type']
    #     user.date_of_provisional_reg = response_data['year_of_provisional']
    #     user.category = response_data['category']
    #     print("response_data inside save():", response_data)
    #     # user.verification_status = response_data.get('verification_status', None)
    #     # user.verification_status = response_data.get('verification_status')
    #     # user.contact = response_data.get('phone', None)
    #     # user.register_type = response_data.get('register_type')
    #     # user.date_of_provisional_reg = response_data.get('year_of_provisional')
    #     # user.category = response_data.get('category')
    #     # user.verification_status = self.response_data['verification_status']
    #     # user.contact = self.response_data['phone']
    #     # user.register_type = self.response_data['register_type']
    #     # user.date_of_provisional_reg = self.response_data['year_of_provisional']
    #     # user.category = self.response_data['category']
    #     user = super().save(request)
    #     return user

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     response_data = cache.get(self.cleaned_data["mdc_registration_no"])

    #     user.first_name = self.cleaned_data["first_name"]
    #     user.last_name = self.cleaned_data["last_name"]
    #     user.username = self.cleaned_data["username"]
    #     user.email = self.cleaned_data["email"]
    #     user.register_as = self.cleaned_data["register_as"]
    #     user.mdc_registration_no = self.cleaned_data["mdc_registration_no"]

    #     if response_data:
    #         user.verification_status = response_data.get('verification_status')
    #         user.contact = response_data.get('phone')
    #         user.register_type = response_data.get('register_type')
    #         user.date_of_provisional_reg = response_data.get('year_of_provisional')
    #         user.category = response_data.get('category')

    #     if commit:
    #         user.save()

    #     return user

    # def save(self):
    #     # user = super().save()
    #     response_data = cache.get(self.cleaned_data["mdc_registration_no"])
    #     response_data.pop('status')
    #     user = User(**self.cleaned_data)
    #     # user.first_name = self.cleaned_data["first_name"]
    #     # user.last_name = self.cleaned_data["last_name"]
    #     # user.username = self.cleaned_data["username"]
    #     # user.email = self.cleaned_data["email"]
    #     # user.register_as = self.cleaned_data["register_as"]
    #     # user.mdc_registration_no = self.cleaned_data["mdc_registration_no"]

    #     # if response_data:
    #     #     user.verification_status = response_data.get('verification_status')
    #     #     user.contact = response_data.get('phone')
    #     #     user.register_type = response_data.get('register_type')
    #     #     user.date_of_provisional_reg = response_data.get('year_of_provisional')
    #     #     user.category = response_data.get('category')

    #     user.save()

    #     return user

    def save(self, request):
        user = super().save(request)

        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        user.register_as = self.cleaned_data["register_as"]
        user.mdc_registration_no = self.cleaned_data["mdc_registration_no"]

        # retrieve response_data from cache
        response_data = cache.get(self.cleaned_data["mdc_registration_no"])

        user.verification_status = response_data.get("verification_status")
        user.contact = response_data.get("phone")
        user.register_type = response_data.get("register_type")
        user.date_of_provisional_reg = response_data.get("year_of_provisional")
        user.category = response_data.get("category")

        user.save()

        return user


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
