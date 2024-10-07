import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class DpiLicenses(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    description = models.TextField(_("Description"), blank=True)

    uuid = models.UUIDField(_("UUID"), default=uuid.uuid4, editable=False, unique=True)
    license = models.TextField(_("License"))

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = "dpi_licenses"
        verbose_name = "DPI License"
        verbose_name_plural = "DPI Licenses"

    def __str__(self):
        return "%s" % self.name
