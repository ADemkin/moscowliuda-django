from django.contrib import admin
from .models import TextBook, Photo, Url, Project


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_projects', 'get_textbooks')
    search_fields = ('name',)

    def get_projects(self, obj):
        return ", ".join([p.title for p in obj.projects.all()])

    get_projects.short_description = 'Проекты'

    def get_textbooks(self, obj):
        return ", ".join([tb.title for tb in obj.text_books.all()])

    get_textbooks.short_description = 'Учебники'


class UrlAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'get_projects', 'get_textbooks')
    search_fields = ('name', 'url')

    def get_projects(self, obj):
        return ", ".join([p.title for p in obj.projects.all()])

    get_projects.short_description = 'Проекты'

    def get_textbooks(self, obj):
        return ", ".join([tb.title for tb in obj.text_books.all()])

    get_textbooks.short_description = 'Учебники'


class TextBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'price_rub', 'created_at')
    filter_horizontal = ('secondary_photos', 'urls')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'created_at')
    filter_horizontal = ('secondary_photos', 'urls')


admin.site.register(Project, ProjectAdmin)
admin.site.register(TextBook, TextBookAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Url, UrlAdmin)
