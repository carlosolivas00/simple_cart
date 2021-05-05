from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.FloatField(validators=[MinValueValidator(.1)])
    created_by = models.CharField(max_length=50, blank=True)
    date_created = models.DateField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    date_added = models.DateField(default=timezone.now, blank=True)


