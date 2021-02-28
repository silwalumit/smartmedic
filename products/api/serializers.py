from rest_framework import serializers
from products.models import (Product, GenericName)
from contacts.api.serializers import ManufacturerSerializer
from contacts.models import Manufacturer
from django.shortcuts import get_object_or_404


class GenericNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenericName
        exclude = (
            "updated_date",
            "created_by",
        )

        read_only_fields = ("created_date",)

class ProductSerializer(serializers.ModelSerializer):
    generic_name = GenericNameSerializer(read_only=True)
    brand = ManufacturerSerializer(read_only=True)
    brand_id = serializers.UUIDField(required=True, write_only=True)
    generic_name_id = serializers.UUIDField(required=True, write_only=True)

    class Meta:
        model = Product
        exclude = (
            "updated_date", 
            "created_by", 
        )

        read_only_fields = ("created_date",) 

    def create(self, validate_data):
        brand_id = validate_data.pop('brand_id')
        generic_name_id = validate_data.pop('generic_name_id')

        brand = get_object_or_404(Manufacturer, id = str(brand_id))
        generic_name = get_object_or_404(GenericName, id=str(generic_name_id))
        
        return Product.objects.create(
            brand=brand,
            generic_name=generic_name,
            **validate_data
        )


