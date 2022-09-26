from django.contrib import admin
from .models import ImageAlbum, Image, Category, Product


class ImageInLine(admin.StackedInline):
    model = Image


@admin.register(ImageAlbum)
class ImageAlbumAdmin(admin.ModelAdmin):
    inlines = [ImageInLine, ]

    def has_module_permission(self, request):
        return False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('article_name', 'price', 'name')
    list_filter = ('category__name',)
