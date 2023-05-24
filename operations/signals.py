from os import remove

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from PIL import Image

from operations.models import Payment, Income, Outcome


@receiver(post_save, sender=Income)
@receiver(post_save, sender=Outcome)
def image_compressor(sender, instance, **kwargs):
    """Signal to compress the image to 1/10 it's size
    Tested with: JPEG
    """
    if kwargs["created"]:
        with Image.open(instance.image.path) as photo:
            photo.save(instance.image.path, optimize=True, quality=10)


@receiver(post_delete, sender=Income)
@receiver(post_delete, sender=Outcome)
def image_delete(sender, instance, **kwargs):
    """Signal to delete the image once it has been deleted"""
    remove(instance.image.path)