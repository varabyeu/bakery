from django.urls import path
from .views import ProductListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<pk>/', ProductDetailView.as_view(), name='product'),
]
