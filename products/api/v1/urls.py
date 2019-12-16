from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ProductApiView.as_view(), name='product_api_view'),
    path('detail/<int:id>', ProductDetailApiView.as_view(), name='product_detail_api_view'),
]