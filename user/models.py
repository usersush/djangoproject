import os
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utilities.utils import rotate_image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dp = models.ImageField(default='default.jpg', upload_to='profile_pic')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.dp.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.dp.path)


@receiver(post_save, sender=Profile)
def get_dp_path(sender, instance, **kwargs):
    if instance.dp:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        fullpath = BASE_DIR + instance.dp.url
        rotate_image(fullpath)
