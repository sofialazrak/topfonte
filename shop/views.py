from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ProductType, ProductAttribute
from cart.forms import CartAddProductForm
import collections, itertools
import json
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.


def product_list(request, category_slug=None):
    category = None
    # categories = Category.objects.all()
    # categories = Category.objects.filter(parent_category__isnull=False).order_by('name')
    categories = Category.objects.filter(parent_category__slug=category_slug).order_by('name')

    # products = Product.objects.filter(available=True)
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        # products = products.filter(category=category)
        products = products.filter(category__parent_category__slug=category_slug)
    return render(
        request,
        'shop/product/list.html',
        {'category' : category, 'categories' : categories, 'products' : products}
    )

def product_detail(request, id, slug):
    # product = get_object_or_404(Product, id=id, slug=slug, available=True)
    product = get_object_or_404(Product, id=id, slug=slug)
    product_types = ProductType.objects.filter(product=product, available=True)
    mylist = []
    lst = []
    for product_type in product_types:
        # mylist.append(dict((x.base, x.value) for x in ProductAttribute.objects.filter(product_type=product_type)))
        
        lst = dict((x.base, x.value) for x in ProductAttribute.objects.filter(product_type=product_type))
        lst = dict(sorted(lst.items(), key=lambda item: item[0]))
        mylist.append(lst)
    
    category = Category.objects.get(id=product.category.id)
    parent_category = category.parent_category
    cart_product_form = CartAddProductForm()
    return render(
        request,
        'shop/product/detail.html',
        {'parent_category':parent_category, 'category':category, 'product': product, 'cart_product_form': cart_product_form, 
        'product_types': product_types, 'mylist': mylist})

def load_product_type(request):
    product_type_id = request.GET.get('product_type_pk')
    product_type = ProductType.objects.get(id=product_type_id)
    return render(request, 'shop/product/price.html', {'product_type': product_type})

