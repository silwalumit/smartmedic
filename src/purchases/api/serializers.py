from rest_framework import serializers
from purchases.models import (PurchaseInvoice, PurchaseDetail)
from django.db import transaction
from products.models import Product
from django.db.models import F
import code

class PurchaseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseDetail
        exclude = (
            'updated_date',
            'created_by',
            'invoice',
        )
    
    def update(self, instance, validated_data):      

        #update product stock info      
        product = Product.objects.get(id = instance.product)
        product.quantity += validated_data.get("quantity", product.quantity) - instance.quantity 
        product.mrp = validated_data.get("mrp", product.mrp)
        product.unit_price = validated_data.get("unit_price", product.unit_price)
        product.save(update_fields = ('quantity', 'mrp','unit_price',))
        
        product.save()
        
        #update purchase invoice amount
        quantity = validated_data.get("quantity", instance.invoice.quantity)
        unit_price = validated_data.get("unit_price", instance.invoice.unit_price)
        
        instance.invoice.amount += quantity * unit_price - instance.quantity * instance.unit_price
        instance.invoice.save(update_fields = ('amount',))
        
        return super().update(instance, validated_data)

class PurchaseInvoiceSerializer(serializers.ModelSerializer):
    items = PurchaseDetailSerializer(many = True, write_only=True)
    
    class Meta:
        model = PurchaseInvoice
        fields = (
            "id",
            "items", 
            "invoice_date", 
            "created_date", 
            "supplier",
            "amount"
        )
        read_only_fields = ('created_date',)

    def create(self, validate_data):
        with transaction.atomic():
            items = validate_data.pop("items")
            invoice = PurchaseInvoice.objects.create(**validate_data)
            
            for item in items:
                product = item.pop("product")
                PurchaseDetail.objects.create(
                    invoice = invoice, 
                    created_by = validate_data.get("created_by"),
                    product = product,
                    **item
                )
                
                product.quantity += item.get("quantity")
                product.mrp = item.get("mrp")
                product.unit_price = item.get("unit_price")
                product.save()

                # Product.objects.filter(id = product.id).update(
                #     quantity = F("quantity")+item.get("quantity"),
                #     mrp = item.get("mrp")
                # )
            return invoice


class PurchaseInvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseInvoice
        fields = ("invoice_date", "supplier", "amount")
