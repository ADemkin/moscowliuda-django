from django.contrib import admin
from .models import Good, Photo, Url, Project


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_project', 'get_good')
    search_fields = ('name',)

    def get_project(self, obj):
        return obj.project.title if obj.project else None

    get_project.short_description = 'Проект'

    def get_good(self, obj):
        return obj.good.title if obj.good else None

    get_good.short_description = 'Пособие'


class UrlAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'get_project', 'get_good')
    search_fields = ('name', 'url')

    def get_project(self, obj):
        return obj.project.title if obj.project else None

    get_project.short_description = 'Проект'

    def get_good(self, obj):
        return obj.good.title if obj.good else None
    get_good.short_description = 'Пособие'


class GoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'price_rub', 'created_at')
    readonly_fields = ['formatted_text']

    def formatted_text(self, obj):
        return obj.formatted_text

    formatted_text.allow_tags = True


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'created_at')
    readonly_fields = ['formatted_text']

    def formatted_text(self, obj):
        return obj.formatted_text

    formatted_text.allow_tags = True


admin.site.register(Project, ProjectAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Url, UrlAdmin)
