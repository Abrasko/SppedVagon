from django import forms
from login.models import User_based as User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['user_name', 'password1', 'password2', ]

    def save(self, commit=True):
        new_user = super().save(commit=False)
        new_user.public_name = new_user.user_name
        new_user.date_of_register = timezone.now()
        if commit:
            new_user.save()
        # self.save_m2m()
        return new_user
