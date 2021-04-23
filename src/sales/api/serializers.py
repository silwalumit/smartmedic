from rest_framework import serializers
from sales.models import SalesInvoice, Sales
from products.models import Product
from django.db import transaction


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        exclude = (
            'updated_date',
            'created_by',
            'invoice',
        )



class SalesInvoiceSerializer(serializers.ModelSerializer):
    items = SalesSerializer(many=True, write_only=True)

    class Meta:
        model = SalesInvoice
        fields = (
            "id",
            "items",
            "created_date",
            "sales_date",
            "customer",
            "amount",
            "discount_on_invoice",
            "discount"
        )

        read_only_fields = ('created_date',)

       

    def create(self, validate_data):
        with transaction.atomic:
            items = validate_data.pop("items")
            instance = SalesInvoice.objects.create(**validate_data)

            for item in items:
                product = item.pop("product")
                Sales.objects.create(
                    invoice=instance,
                    created_by=validate_data.get("created_by"),
                    product=product,
                    **item
                )
            return instance
