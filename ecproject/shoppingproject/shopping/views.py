from django.shortcuts import render, get_object_or_404
from django.http import Http404,HttpResponseRedirect
from django.template.response import TemplateResponse
from shopping.models import Product
from django.urls import reverse


def product_list(request):
    products = Product.objects.order_by('name')
    return TemplateResponse(request, 'shopping/product_list.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shopping/product_detail.html', {'product': product})


def cart_add(request, product_id):
    if not Product.objects.filter(id=product_id).exists():
        raise Http404
    
    cart = request.session.get('cart')
    if cart:
        cart.append(product_id)
        request.session['cart'] = cart
    else:
        request.session['cart'] = [product_id]
    return HttpResponseRedirect(reverse('product_list'))
    

def product_cart(request):
    cart = request.session.get('cart')
    if cart:
        products = []
        for product_id in cart:
            try:
                product = Product.objects.get(id=product_id)
                products.append(product)
            except Product.DoesNotExist:
                pass
    else:
        products = []
    
    total_price = 0
    for product in products:
        total_price += product.price

    return TemplateResponse(request,
                             'shopping/product_cart.html',
                               {'products': products,
                                'total_price': total_price})


def cart_delete(request, product_id):
    cart = request.session.get('cart')
    if cart:
        filtered = []
        for p in cart:
            if p != product_id:
                filtered.append(p)
        request.session['cart'] = filtered
    return HttpResponseRedirect(reverse('product_cart'))

