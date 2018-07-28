from django import forms
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from login.models import User_based as User
from mychar.models import CharPost, CharPhoto
from django.utils import timezone


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_email', 'public_name', ]


class EditProfilePasswordForm(PasswordChangeForm):
    pass


class AddPostForm(forms.ModelForm):
    class Meta:
        model = CharPost
        fields = ['post_text']

    def save(self, user_viewer, commit=True):
        new_post = super().save(commit=False)
        new_post.post_author = user_viewer
        new_post.post_date = timezone.now()
        if commit:
            new_post.save()
        # self.save_m2m()
        return new_post


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = CharPhoto
        fields = ['image']

    def save(self, user, commit=True):
        new_photo = super().save(commit=False)
        new_photo.photo_author = user
        new_photo.photo_date = timezone.now()
        new_photo.is_char_photo = True
        if commit:
            new_photo.save()
        return new_photo
