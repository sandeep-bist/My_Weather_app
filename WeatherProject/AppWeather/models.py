from django.db import models
from django.urls import reverse

# Create your models here.
class City(models.Model):
    city= models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural ='cities'
        ordering = ['-timestamp']
