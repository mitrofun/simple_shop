from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView, TemplateView

from apps.cart.cart import Cart
from apps.category.models import Product
from . import forms


class CartDetail(TemplateView):
    template_name = 'cart/index.html'

    def get_context_data(self, **kwargs):
        context = super(CartDetail, self).get_context_data(**kwargs)
        cart = Cart(self.request)
        context['page_title'] = 'Корзина'
        for item in cart:
            item['update_quantity_form'] = forms.CartAddProductForm(
                initial={
                    'quantity': item['quantity'],
                    'update': True
                })
        return context


class ProductAddInCartView(FormView):
    form_class = forms.CartAddProductForm
    success_url = reverse_lazy('cart:detail')

    def form_valid(self, form):
        cart = Cart(self.request)
        product = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        quantity = form.cleaned_data['quantity']
        update = form.cleaned_data['update']
        cart.add(product=product, quantity=quantity, update_quantity=update)
        return super(ProductAddInCartView, self).form_valid(form)


class ProductDeleteInCartView(RedirectView):
    pattern_name = 'cart:detail'

    def get_redirect_url(self, *args, **kwargs):
        cart = Cart(self.request)
        product = get_object_or_404(Product, pk=kwargs['product_id'])
        cart.remove(product)
        kwargs.clear()
        return super(ProductDeleteInCartView, self).get_redirect_url(*args, **kwargs)
