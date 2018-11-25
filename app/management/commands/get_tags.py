from django.core.management.base import BaseCommand
from app.utils import created_tags_for_service, created_tags_for_product
from app.models import Service, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        products = Product.objects.all()
        for product in products:
            created_tags_for_product(product)

        services = Service.objects.all()
        for service in services:
            created_tags_for_service(service)
