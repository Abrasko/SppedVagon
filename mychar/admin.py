from django.contrib import admin
from .models import CharPost, CharPostComment, AllSkillsList
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from login.models import User_based as User
from mychar.models import UserSkillsList
# Register your models here.

class CharPostCommentInline(admin.TabularInline):
    model = CharPostComment
    extra = 1

class CharPostChangeForm(forms.ModelForm):
    class Meta:
        model = CharPost
        fields = ('post_author', 'post_date', 'post_text')

class CharPostAdmin(admin.ModelAdmin):
    form = CharPostChangeForm
    fieldsets = [
        ('Post',                  {'fields':  ['post_author', 'post_text'] }),
        ('Date information',        {'fields':  ['post_date'],  }),
            ]
    inlines = [CharPostCommentInline]
    list_display = ('post_author', 'post_date')
    list_filter = ['post_date']
    search_fields = ['post_text']

admin.site.register(AllSkillsList)
admin.site.register(CharPost, CharPostAdmin)
# admin.site.register(ProfileParams)
