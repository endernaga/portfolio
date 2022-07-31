from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class RubricksAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'parent')
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'slug', 'parent')
    list_filter = ('name', 'parent')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class TagsAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'slug')
    list_filter = ('name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class CommentAdmin(admin.ModelAdmin):
    fields = ('post', 'name', 'text')
    list_display = ('id','post', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('text',)


class ProductsAdmin(admin.ModelAdmin):
    fields = ('name', 'describe', 'slug', 'photo', 'tag', 'rubrick', 'price', 'avaibility', 'if_vip')
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'slug', 'get_photo')
    list_filter = ('name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)

    def get_photo(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width=50px>')

admin.site.register(Rubricks, RubricksAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Products, ProductsAdmin)