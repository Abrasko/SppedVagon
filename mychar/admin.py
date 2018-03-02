from django.contrib import admin
from .models import BasePost, BaseComment, AllSkillsList
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class CommentsInline(admin.TabularInline):
    model = BaseComment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post',                  {'fields':  ['post_author', 'post_text'] }),
        ('Date information',        {'fields':  ['post_date'],  }),
            ]
    inlines = [CommentsInline]
    list_display = ('post_author', 'post_date')
    list_filter = ['post_date']
    search_fields = ['post_text']

class PostAdminss(admin.ModelAdmin):
    fieldsets = [
        ('Post',                  {'fields':  ['post_author', 'post_text'] }),
        ('Date information',        {'fields':  ['post_date'],  }),
            ]
    inlines = [CommentsInline]
    list_display = ('post_author', 'post_date')
    list_filter = ['post_date']
    search_fields = ['post_text']

# admin.site.register(CommentsBased)
# class ProfileParamsChangeForm(forms.ModelForm):
#     class Meta:
#         model = ProfileParams
#         fields = ('date_of_register', 'city')

# class ProfileParamsAdmin(BaseUserAdmin):
#     form = ProfileParamsChangeForm

#     list_display = ('holder', 'date_of_register', 'city',)
#     list_filter = ('holder',)

#     fieldsets = (
#         (None,              {'fields': ('date_of_register', 'city')}),
#     )

#     search_fields = ('holder',)
#     ordering = ('holder',)
#     filter_horizontal = ()



admin.site.register(AllSkillsList)
admin.site.register(BasePost, PostAdmin)
# admin.site.register(ProfileParams)

