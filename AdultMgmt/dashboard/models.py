from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Bills(models.Model):
    name = models.TextField()
    date = models.DateField(default=date.today)
    bill_type = models.TextField()
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    comment = models.TextField(blank=True, null=True)
    paid_by = models.TextField()

    def __unicode__(self):
        return u" %s" % self.date



