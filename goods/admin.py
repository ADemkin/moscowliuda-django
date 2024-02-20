from django.contrib import admin
from .models import TextBook, Photo, Url


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_text_books')
    search_fields = ('name',)

    def get_text_books(self, obj):
        return ", ".join([tb.title for tb in obj.text_books.all()])

    get_text_books.short_description = 'Учебники'


class UrlAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'get_text_books')
    search_fields = ('name', 'url')

    def get_text_books(self, obj):
        return ", ".join([tb.title for tb in obj.text_books.all()])

    get_text_books.short_description = 'Учебники'


class TextBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'price_rub', 'created_at')
    filter_horizontal = ('secondary_photos', 'urls')


admin.site.register(TextBook, TextBookAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Url, UrlAdmin)
