from rest_framework import serializers
from contacts.models import Distributor, Manufacturer, Customer

class DistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        exclude = (
            "updated_date",
            "created_by",
        )

        read_only_fields = ("created_date",)

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        exclude = (
            "updated_date",
            "created_by",
        )

        read_only_fields = ("created_date",)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = (
            "updated_date",
            "created_by",
        )

        read_only_fields = ("created_date",)
