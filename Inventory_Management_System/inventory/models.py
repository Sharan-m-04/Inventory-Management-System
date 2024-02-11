from django.db import models

# Create your models here.
class Product(models.Model):
    prod_id = models.IntegerField(primary_key=True)
    prod_name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.prod_name
    class Meta:
        db_table = 'products'