from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    brand = models.ForeignKey('brands.Brand', on_delete=models.PROTECT, related_name='products')
    category = models.ForeignKey('categories.Category', on_delete=models.PROTECT, related_name='products')
    description = models.TextField(blank=True, null=True)
    serie_number = models.CharField(max_length=100, unique=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['title']
    
    def __str__(self):
        return self.name