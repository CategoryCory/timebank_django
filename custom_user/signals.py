from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver

CustomUser = get_user_model()


@receiver(pre_save, sender=CustomUser)
def set_is_active_to_false(sender, instance, **kwargs):
    if instance.id is None:
        instance.is_active = False
