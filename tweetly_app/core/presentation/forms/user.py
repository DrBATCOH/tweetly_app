from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

User = get_user_model()


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "country", "birthdate")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["placeholder"] = "First Name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["country"].widget.attrs["placeholder"] = "Country"
        self.fields["birthdate"].widget.attrs["placeholder"] = "Birthdate"
