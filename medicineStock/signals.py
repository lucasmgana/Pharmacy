from django.db.models.signals import post_save
from django.dispatch import receiver
from medicineStock.models import Stock, Purchase

@receiver(post_save, sender = Stock)
def post_save_created_farmer(sender, instance, created, **kwargs):
    if created:
        Purchase.objects.create(
            stock_name =instance.medicine_id, 
            buying_price = instance.buying_price,
            added_by= instance.added_by,
            quantity= instance.quantity,
            expire_date = instance.expire_date,
            selling_price= instance.selling_price,
            )
            