from django.db import models


class Store(models.Model):
    store_name = models.CharField(max_length=50, null=True, blank=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(max_length=50, null=True, blank=True)

    def __str__(self):
      return str(self.store_name)
