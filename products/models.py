from django.db import models
# Create your models here.
class Product(models.Model):
    
    name = models.CharField(max_length=254, default='')
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    old_price = models.DecimalField(max_digits=6, decimal_places=2)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images')
    
    class Meta:
        unique_together = ('name','slug')

    def __str__(self):
        return self.slug
        
