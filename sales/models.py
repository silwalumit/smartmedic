from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from core.abstract_models import AbstractTimeStampModel

class SalesInvoice(AbstractTimeStampModel):
    customer = models.ForeignKey(
        "contacts.Customer", 
        verbose_name=_("Customer"), 
        on_delete=models.SET_NULL,
        null = True
    )
    sales_date = models.DateField(_("Date"))
    amount = models.DecimalField(
        _("Invoice Amount"), 
        max_digits=8, 
        decimal_places=2
    )
    discount_on_invoice = models.BooleanField(_("Discount on Invoice"), default = False)
    discount = models.FloatField(_("Discount"), default = 0.0)

class Sales(AbstractTimeStampModel):
    invoice = models.ForeignKey(
        "sales.SalesInvoice", 
        verbose_name=_("Invoice"), 
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "products.Product",
        verbose_name = _("Product"),
        on_delete = models.PROTECT,
    )
    quantity = models.IntegerField(_("Quantity"),)
    
    discount = models.FloatField(_("Discount"), default = 0.0)
    
    unit_price = models.DecimalField(
        _("Sales Amount"),
        max_digits=8,
        decimal_places=2
    )
