from django.urls import path

from .views import *

urlpatterns = [
    path('', ProductApiView.as_view(), name='product_api_view'),
    path('detail/<int:id>', ProductDetailApiView.as_view(), name='product_detail_api_view'),
    path('tracking', TrackingApiView.as_view(), name='tracking_api_view'),
    path('tracking/detail/<str:id>', TrackingDetailApiView.as_view(), name='tracking_detail_api_view'),
]