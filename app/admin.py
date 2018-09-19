from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models

admin.site.register(models.ProductUse)
admin.site.register(models.ProductFeature)


@admin.register(models.ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):

    fields = ["product", "photo", "photo_view"]
    readonly_fields = ('photo_view',)

    def photo_view(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.photo.url,
            width=200,
            height=150,
            )
    )


class ProductPhotoRelativeAdmin(admin.StackedInline):
    model = models.ProductPhoto

    readonly_fields = ('photo_view',)

    def photo_view(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.photo.url,
            width=200,
            height=150,
        )
        )


class ProductUseRelativeAdmin(admin.TabularInline):
    model = models.ProductUse.products.through


class ProductFeatureRelativeAdmin(admin.TabularInline):
    model = models.ProductFeature.products.through


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductPhotoRelativeAdmin, ProductUseRelativeAdmin, ProductFeatureRelativeAdmin]