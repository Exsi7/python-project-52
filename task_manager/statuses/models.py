from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Status(models.Model):
    name = models.CharField(_("name"), max_length=50)
    created_at = models.DateTimeField(_("created at"), auto_now=True)

    def __str__(self):
        return self.name