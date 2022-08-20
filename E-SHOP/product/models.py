from django.db import models
from product.utils import product_image_file_path


class Product(models.Model):
    product_name = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(max_length=250, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0.00, null=True, blank=True)
    stock = models.BooleanField(default=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to=product_image_file_path)
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
