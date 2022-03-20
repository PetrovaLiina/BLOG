from django.contrib import admin

from .models import Portal, Category


class PortalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'post')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published',)


class СategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Portal, PortalAdmin)
admin.site.register(Category, СategoryAdmin)
