from django.contrib import admin

from .models import Group, Post


@admin.register
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'description',
        'slug',
    )
    search_fields = ('title', 'description')
    list_filter = ('title',)
    empty_value_display = '-пусто-'


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
    list_editable = ('group',)



