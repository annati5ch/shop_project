from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.http import Http404
#from django.http import HttpResponse

def product_detail(request, product_id, product_slug):
    product = get_object_or_404(Product,
                                id=product_id,
                                slug=product_slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, '/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})

def home_page(request):
    photo = Product.image
    name = Product.name
    old_price = Product.orig_price
    discount = Product.discount
    sell_price = Product.sell_price

    return render(request, 'home_page.html',
                  {'photo': photo,
                   'old_price': old_price,
                   'name': name,
                   'discount': discount,
                   'sell_price': sell_price})

def product_list(request):
    queryset = Product.objects.all()
    context = {'products': queryset}
    return render(request, "product/product_list.html", context)

def product_list_categories(request):
    object_list = Category.objects.values_list('name', flat=True).distinct()
    context = {'object_list': object_list}
    return render(request,"product/product_list.html", context)




