from django.db.models.signals import pre_save
from django.dispatch import receiver
from order.utils import unique_order_id_generator
from order.models import Order


@receiver(pre_save, sender=Order)
def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id= unique_order_id_generator(instance)
