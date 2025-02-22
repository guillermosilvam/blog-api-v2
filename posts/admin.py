from django.contrib import admin
from .models import post

# Register your models here.
class postAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_posted', 'updated', 'author')
    list_filter = ('date_posted', 'author')
    search_fields = ('title', 'content', 'author__username')
    ordering = ('-date_posted',)

admin.site.register(post, postAdmin)