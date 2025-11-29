from django.db import models

# Create your models here.
class Outflow(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT, related_name='outflows')
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Outflow'
        verbose_name_plural = 'Outflows'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Outflow of {self.quantity} units of {self.product.title} on {self.created_at.strftime("%Y-%m-%d")}'