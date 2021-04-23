from django.urls import path
from .views import (
    ProductListAPIView, 
    ProductDetailAPIView,
    GenericNameListAPIView,
    GenericNameDetailAPIView
)

urlpatterns = [
    path('', ProductListAPIView.as_view()),
    path('/<uuid:pk>', ProductDetailAPIView.as_view()),
    path('/generic-name', GenericNameListAPIView.as_view()),
    path('/generic-name/<uuid:pk>', GenericNameDetailAPIView.as_view())
]