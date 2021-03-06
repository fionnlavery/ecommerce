from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.


def all_products(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request, "products.html", context)
    
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "productdetail.html", {'product':product})
    
