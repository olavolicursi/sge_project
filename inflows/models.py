from django.db import models

# Create your models here.
class Inflow(models.Model):
    supplier = models.ForeignKey('suppliers.Supplier', on_delete=models.PROTECT, related_name='inflows')
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT, related_name='inflows')
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Inflow'
        verbose_name_plural = 'Inflows'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Inflow of {self.quantity} units of {self.product.title} from {self.supplier.name} on {self.created_at.strftime("%Y-%m-%d")}'