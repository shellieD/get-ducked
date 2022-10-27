from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LKH8SAWtvFHMlJiXxWx0rw1PA5yXUBFguXq5Ch0Vcuj9MJCd5XrjP9C1VHsAVOyBqyP8v6uQWUr2oz9rEcr3lWk00K6aDxtQm',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
