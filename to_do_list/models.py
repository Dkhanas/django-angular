from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _


class ToDoList(models.Model):
    name = models.CharField(max_length=20, default='', verbose_name=_("Name"))
    checked = models.BooleanField(default=False, verbose_name=_("Checked"))
    description = models.TextField(
        default='', max_length=2000, verbose_name=_("Description")
    )
    date_created = models.DateTimeField(auto_now_add=True,
                                        verbose_name=_("Date created"))
    date_modified = models.DateTimeField(auto_now_add=True,
                                         verbose_name=_("Date modified"))

    def __unicode__(self):
        return self.name