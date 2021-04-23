from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.abstract_models import AbstractTimeStampModel

# class PurchaseManager(models.Manager):
#     def create(self):
            

class PurchaseInvoice(AbstractTimeStampModel):
    supplier = models.ForeignKey(
        "contacts.Distributor", 
        on_delete=models.PROTECT
    )

    invoice_date = models.DateField(
        _("Invoice Date"),
    )

    amount = models.DecimalField(
        _("Amount"), 
        max_digits=8, 
        decimal_places=2,
    )

    discount_received = models.DecimalField(
        _("Discount Received"),
        max_digits=7,
        decimal_places=2,
        default=0.0
    )


    class Meta:
        verbose_name = "Purchase Invoice"
        verbose_name_plural = "Purchase Invoices"

class PurchaseDetail(AbstractTimeStampModel):
    invoice = models.ForeignKey(
        "purchases.PurchaseInvoice",
        related_name="items",
        related_query_name = "item",
        on_delete = models.CASCADE
    )
    product = models.ForeignKey(
        verbose_name = _("Product"),
        to = "products.Product",
        on_delete = models.PROTECT
    )
    bonus_quantity = models.IntegerField(_("Bonus"), default=0)

    quantity = models.IntegerField(_("Quantity"),)

    unit_price = models.DecimalField(
        _("Unit Price"),
        max_digits=6,
        decimal_places=2,
    )

    mrp = models.DecimalField(
        _("Maximum Retail Price"),
        max_digits=6,
        decimal_places=2,
    )
    expires_on = models.DateField(_("Expiry Date"))
    batch_no = models.CharField(_("Batch No"), max_length=20)
    
    cc_charge = models.FloatField("CC Charge", null = True)
    cc_charge_amount = models.IntegerField(null = True)

    excise = models.FloatField(_("Excise Duty"), default = 0.0)

    discount_received = models.FloatField(_("Discount Received"), default = 0.0)

    class Meta:
        verbose_name = "Purchase Item"
        verbose_name_plural = "Purchase Items"
