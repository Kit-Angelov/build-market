from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


@admin.register(models.StorePhoto)
class StorePhotoAdmin(admin.ModelAdmin):

    fields = ["store", "photo", "photo_view"]
    readonly_fields = ('photo_view',)

    def photo_view(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.photo.url,
            width=200,
            height=150,
            )
    )


class StorePhotoRelativeAdmin(admin.StackedInline):
    model = models.StorePhoto

    readonly_fields = ('photo_view',)

    def photo_view(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.photo.url,
            width=200,
            height=150,
        )
    )


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    inlines = [StorePhotoRelativeAdmin, ]


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


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductPhotoRelativeAdmin,]