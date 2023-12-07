from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class SortendURL(models.Model):
    url = models.CharField(max_length=200)
    qr_code = models.ImageField(blank=True,name="qr_code",upload_to="public/qrcode")

