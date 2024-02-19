from django.contrib import admin
from goods.models import TextBookPhoto, YoutubeUrl, TextBook, Project


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo')
    search_fields = ('name',)


class TextBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'price_rub', 'created_at')
    search_fields = ('title', 'sub_title', 'description')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'created_at')
    search_fields = ('title', 'sub_title', 'description')


class YoutubeUrlAdmin(admin.ModelAdmin):
    list_display = ('url',)
    search_fields = ('url',)
    filter_horizontal = ('books', 'projects')


admin.site.register(Project, ProjectAdmin)
admin.site.register(TextBook, TextBookAdmin)
admin.site.register(YoutubeUrl, YoutubeUrlAdmin)
admin.site.register(TextBookPhoto, PhotoAdmin)
