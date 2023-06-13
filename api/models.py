from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200, null=False, blank=True)
    category=models.CharField(max_length=200, null=False, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description=models.TextField()
    start=models.IntegerField()

    def _str_(self):
        return self.name