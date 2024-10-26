from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from .models import Artwork, Book, Photo, BookImage, ArtworkImage


class ArtworkAdmin(ModelAdmin):
    ordering = ['-year', 'title_cz']
    list_display = ['id', 'title_cz', 'title_en', 'year', 'category', 'technique', 'material', 'dimensions']
    list_display_links = ['id', 'title_cz', 'title_en']
    list_filter = ['category', 'year', 'dimensions']
    search_fields = ['title_cz', 'title_en', 'material']
    list_per_page = 20


class BookAdmin(ModelAdmin):
    ordering = ['-year', 'title_cz']
    list_display = ['id', 'title_cz', 'title_en', 'author', 'publisher', 'year', 'category']
    list_display_links = ['id', 'title_cz', 'title_en']
    list_filter = ['category', 'year']
    search_fields = ['title_cz', 'title_en']
    list_per_page = 20


class PhotoAdmin(ModelAdmin):
    ordering = ['-year', 'title_cz']
    list_display = ['id', 'title_cz', 'title_en', 'description', 'year']
    list_display_links = ['id', 'title_cz', 'title_en']
    list_filter = ['year']
    search_fields = ['title_cz', 'title_en']
    list_per_page = 20


class BookImageAdmin(ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'book', 'image']
    list_display_links = ['id', 'book']
    search_fields = ['book__title_cz', 'book__title_en']
    list_per_page = 20


class ArtworkImageAdmin(ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'artwork', 'image']
    list_display_links = ['id', 'artwork']
    search_fields = ['artwork__title_cz', 'artwork__title_en']
    list_per_page = 20


admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(BookImage, BookImageAdmin)
admin.site.register(ArtworkImage, ArtworkImageAdmin)