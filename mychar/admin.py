from django.contrib import admin
from .models import PostBased, CommentsBased

# Register your models here.

class CommentsInline(admin.TabularInline):
    model = CommentsBased
    extra = 1

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Author',                  {'fields':  ['post_author'] }),
        ('Date information',        {'fields':  ['post_date'],
                                #  'classes': ['collapse'] 
                            }),
            ]
    inlines = [CommentsInline]
    list_display = ('post_author', 'post_text', 'post_date')
    list_filter = ['post_date']
    search_fields = ['post_text']
    


admin.site.register(PostBased, PostAdmin)
# admin.site.register(CommentsBased)