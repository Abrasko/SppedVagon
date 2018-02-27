from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import SkillsList, ProfileParams
# Register your models here.

class ProfileParamsChangeForm(forms.ModelForm):
    class Meta:
        model = ProfileParams
        fields = ('date_of_register', 'city')

class ProfileParamsAdmin(BaseUserAdmin):
    form = ProfileParamsChangeForm

    list_display = ('holder', 'date_of_register', 'city',)
    list_filter = ('holder',)

    fieldsets = (
        (None,              {'fields': ('date_of_register', 'city')}),
    )

    search_fields = ('holder',)
    ordering = ('holder',)
    filter_horizontal = ()

admin.site.register(ProfileParams, ProfileParamsAdmin)
admin.site.register(SkillsList)
# admin.site.register(ProfileParams)

