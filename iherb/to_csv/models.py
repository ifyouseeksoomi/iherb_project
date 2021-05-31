from django.db import models


class BathPersonalProduct(models.Model):
    key_number = models.IntegerField(default=0, null=True)
    img_src = models.TextField(blank=True, default='')
    name = models.CharField(max_length=300, blank=True, default='')
    rating = models.CharField(max_length=20, blank=True, default='')
    reviews = models.IntegerField(default=0, null=True)
    price = models.CharField(max_length=20, blank=True, default='')
    link = models.TextField(blank=True, default='')

    class Meta:
        db_table = 'bath_personal_products'

    def __str__(self):
        return self.name
