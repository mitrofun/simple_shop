from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('categories/<category_slug>/', views.ProductListView.as_view(), name='category-detail'),
    path('products/<slug>/', views.ProductDetailView.as_view(), name='product-detail'),
]
