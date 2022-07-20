from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'status', 'created_on')
    search_fields = ['name', 'content']
    list_filter = ('created_on',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('content',)
