from django.contrib import admin
from .models import Product

# Register your models here.

# product changes to Admin Panel
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name','description']
    list_display = ['name', 'price', 'active']
    list_editable = ['price','active']
    list_filter = ['price', 'active']
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)