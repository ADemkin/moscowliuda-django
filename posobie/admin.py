from django.contrib import admin

from posobie.models import TextBookPhoto, YoutubeUrl, TextBook


class TextBookPhotoInline(admin.TabularInline):
    model = TextBookPhoto
    extra = 1

class YoutubeUrlInline(admin.TabularInline):
    model = YoutubeUrl.books.through
    extra = 1

class TextBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'price_rub', 'created_at')
    search_fields = ('title', 'sub_title', 'description')
    list_filter = ('created_at', 'price_rub')
    inlines = [TextBookPhotoInline, YoutubeUrlInline]

admin.site.register(TextBook, TextBookAdmin)

class YoutubeUrlAdmin(admin.ModelAdmin):
    list_display = ('url',)
    search_fields = ('url',)
    filter_horizontal = ('books', 'projects')

admin.site.register(YoutubeUrl, YoutubeUrlAdmin)