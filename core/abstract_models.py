import uuid
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class AbstractTimeStampModel(models.Model):
    id = models.UUIDField(_("ID"),primary_key=True, default=uuid.uuid4, editable=False)
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name=_("Created By"), 
        on_delete=models.CASCADE
    )
    
    created_date = models.DateTimeField(_("Created Date"), auto_now_add = True)
    updated_date = models.DateTimeField(_("Updated Date"),auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.created_date)

