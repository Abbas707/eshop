from django.db import models
from user.models import CustomUser
from product.models import Product
from order.constants import ORDER_STATUS
from store.models import Store
from order.managers import OrderManager


class Order(models.Model):
    order_id= models.CharField(max_length=120, null=True, blank= True) 
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS, default=ORDER_STATUS[0][1])
    items = models.ManyToManyField(Product)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = OrderManager.as_manager()

    def __str__(self):
        return self.order_id
