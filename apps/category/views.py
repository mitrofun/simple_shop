from django.views.generic import ListView, DetailView

from apps.cart import forms
from . import models


class ProductListView(ListView):
    model = models.Product
    queryset = models.Product.available_objects.all()
    template_name = 'category/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        if 'category_slug' in self.kwargs:
            queryset = queryset.filter(
                category__slug=self.kwargs['category_slug']
            )
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['active_category'] = self.kwargs.get('category_slug', None)
        return context


class ProductDetailView(DetailView):
    model = models.Product
    queryset = models.Product.available_objects.all()
    template_name = 'category/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['cart_product_form'] = forms.CartAddProductForm
        return context
