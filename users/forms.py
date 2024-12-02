from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from users.models import Complaints


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
            self.fields["username"].help_text = " "
            self.fields["password1"].help_text = " "
            self.fields["password2"].help_text = " "


class UserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "role"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
            self.fields["username"].help_text = " "
            self.fields["password1"].help_text = " "
            self.fields["password2"].help_text = " "


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "role"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
            self.fields["username"].help_text = " "


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = ["report"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class RespondComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = ["respond"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
