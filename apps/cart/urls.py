from django.urls import path

from . import views


urlpatterns = [
    path('', views.CartDetail.as_view(), name='detail'),
    path('add/<product_id>/', views.ProductAddInCartView.as_view(), name='product-add'),
    path('remove/<product_id>/', views.ProductDeleteInCartView.as_view(), name='product-delete'),
]
