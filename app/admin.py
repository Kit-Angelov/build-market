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


class ProductFeaturesRelativeAdmin(admin.StackedInline):
    model = models.ProductFeature


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductPhotoRelativeAdmin, ProductFeaturesRelativeAdmin]


@admin.register(models.ContractorPhoto)
class ContractorPhotoAdmin(admin.ModelAdmin):

    fields = ["contractor", "photo", "photo_view"]
    readonly_fields = ('photo_view',)

    def photo_view(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.photo.url,
            width=200,
            height=150,
            )
    )


class ContractorPhotoRelativeAdmin(admin.StackedInline):
    model = models.ContractorPhoto

    readonly_fields = ('photo_view',)

    def photo_view(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.photo.url,
            width=200,
            height=150,
        )
    )


@admin.register(models.Contractor)
class ContractorAdmin(admin.ModelAdmin):
    inlines = [ContractorPhotoRelativeAdmin, ]


@admin.register(models.ServicePhoto)
class ServicePhotoAdmin(admin.ModelAdmin):

    fields = ["service", "photo", "photo_view"]
    readonly_fields = ('photo_view',)

    def photo_view(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.photo.url,
            width=200,
            height=150,
            )
    )


admin.site.register(models.ServiceWork)


class ServicePhotoRelativeAdmin(admin.StackedInline):
    model = models.ServicePhoto

    readonly_fields = ('photo_view',)

    def photo_view(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.photo.url,
            width=200,
            height=150,
        )
    )


class ServiceWorkRelativeAdmin(admin.StackedInline):
    model = models.ServiceWork


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceWorkRelativeAdmin, ServicePhotoRelativeAdmin]
