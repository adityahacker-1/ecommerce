from django.shortcuts import render
from products.models import Product, Category

# Create your views here.
def get_product(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        context = {'product': product}
        
        if request.GET.get('size'):
            size = request.GET.get('size')
            price = product.get_product_price_by_size(size)
            context['selected_size'] = size
            context['updated_price'] = price
        
        return render(request, 'products/products.html', context=context )
    
    except Exception as e:
        print(e)
        return render(request, 'products/products.html', {'error': 'Product not found'})