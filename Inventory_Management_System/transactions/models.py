from django.db import models
from inventory.models import Product

# Create your models here.
class Transaction(models.Model):
    t_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    prod_name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)
    updated_quantity = models.IntegerField()

    @property
    def formatted_t_id(self):
        return f"invms{self.t_id}"

    class Meta:
        db_table = 'transactions'
