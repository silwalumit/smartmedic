from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from core.abstract_models import AbstractTimeStampModel

class Distributor(AbstractTimeStampModel):
    name = models.CharField(_("Name"),max_length=50)
    address = models.CharField(_("Address"),max_length = 200, null = True)
    pan_no = models.CharField(_("Pan Number"),null = True, max_length=50)
    
    primary_number = models.CharField(
        _("Primary Phone Number"),
        unique=True,
        max_length=10,
        validators=[RegexValidator(regex='^[0-9]{8,}$')],
    )

    secondary_number = models.CharField(
        _("Secondary Phone number"),
        null = True,
        unique=True,
        max_length=10,
        validators=[RegexValidator(regex='^[0-9]{8,}$')],
    )

    class Meta:
        verbose_name = "Distributor"
        verbose_name_plural = "Distributors"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Manufacturer(AbstractTimeStampModel):
    name = models.CharField(_("Name"),max_length=50)
    initials = models.CharField(_("Initials"), max_length=10, null=True)
    license_no = models.CharField(_("License Number"),max_length=50, null = True)


class Customer(AbstractTimeStampModel):
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    mobile_no = models.CharField(
        _("Mobile Number"),
        unique=True,
        max_length=10,
        validators=[RegexValidator(regex='^[0-9]{8,}$')],
    )
