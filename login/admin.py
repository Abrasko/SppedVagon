from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User_based as User
from mychar.models import ProfileParams
# Register your models here.

class ProfileParamsInline(admin.TabularInline):
    model = ProfileParams
    extra = 1

    # inlines = [ChoiceInline]
    # list_display = ('question_text', 'date', 'was_published_recently')
    # list_filter = ['date']
    # search_fields = ['question_text']

class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', 
    widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('user_name', 'user_email', 'public_name')
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=(
            "<a href=\"../password/\">Change password</a>."
        ),
    )

    class Meta:
        model = User
        fields = ('user_name', 'password', 'user_email', 'public_name',
        'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('user_name', 'user_email', 'public_name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None,              {'fields': ('user_name', 'password')}),
        ('Personal info',   {'fields': ('public_name', 'user_email',)}),
        ('Permissions',     {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_name', 'user_email', 'public_name', 'password1', 'password2')}
        ),
    )

    search_fields = ('user_name',)
    ordering = ('user_name',)
    filter_horizontal = ()



admin.site.register(User, UserAdmin)
admin.site.unregister(Group)