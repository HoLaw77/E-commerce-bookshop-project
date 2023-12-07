from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Order, OrderDetail

@receiver(post_save, sender=OrderDetail)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on order detail
    """
    instance.order.generate_total()

@receiver(post_delete, sender=OrderDetail)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on when delete or adjust
    """
    print('delete signal received!')
    instance.order.generate_total()