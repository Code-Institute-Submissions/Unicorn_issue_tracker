from django.shortcuts import render, redirect, reverse, get_object_or_404
from features.views import feature_detail
from features.models import Features
from django.contrib.auth.decorators import login_required


# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    feature = get_object_or_404(Features, id=id)
    feature.views -= 1
    feature.save()

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    cart[id] = quantity
    request.session['cart'] = cart
    return redirect(feature_detail, id)

def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
