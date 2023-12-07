from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class SortendURL(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    user_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=200,name="short url",default="")
    url_visit = models.IntegerField(name="visited url",default=0)
    qr_code = models.ImageField(blank=True,name="qr_code",upload_to="public/qrcode")

