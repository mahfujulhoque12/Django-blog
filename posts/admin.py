from django.contrib import admin
from . models import Post
from modeltranslation.admin import TranslationAdmin
# Register your models here.


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_filter = ['post_type']
    search_fields = ['title', 'author__username']
    list_display =['title','title_de','title_ja',]



    
