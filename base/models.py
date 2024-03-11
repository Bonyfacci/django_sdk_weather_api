from django.db import models
from django.utils.translation import gettext_lazy as _


NULLABLE = {'blank': True, 'null': True}


class BaseModel(models.Model):
    """Base model"""
    objects = None
    created = models.DateTimeField(_('created at'), auto_now_add=True)
    updated = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        abstract = True
