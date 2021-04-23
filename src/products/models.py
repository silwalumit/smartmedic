from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.abstract_models import AbstractTimeStampModel

class Product(AbstractTimeStampModel):
    name = models.CharField(unique = True, max_length = 50)
    ws_unit = models.CharField(_("Wholesale Unit"), max_length=8)

    brand = models.ForeignKey(
        "contacts.Manufacturer",
        verbose_name=_("Brand"),
        on_delete=models.PROTECT,
    )

    generic_name = models.ForeignKey(
        "products.GenericName",
        on_delete=models.PROTECT,
    )

    quantity = models.IntegerField(
        _("Quantity"),
        default = 0
    )

    unit_price = models.DecimalField(
        _("Unit Price"),
        max_digits=6,
        decimal_places=2,
        default = 0.0
    )

    mrp = models.DecimalField(
        _("Maximum Retail Price"),
        max_digits=6,
        decimal_places=2,
        default=0.0,
    )

   
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["name"]

    def __str__(self):
        return self.name


class GenericName(AbstractTimeStampModel):
    name = models.CharField(unique = True, max_length=50)

    class Meta:
        verbose_name = "Generic Name"
        verbose_name_plural = "Generic Names"

    def __str__(self):
        return self.name
