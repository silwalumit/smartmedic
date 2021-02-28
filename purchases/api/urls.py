from django.urls import path
from .views import (
    PurchaseDetailAPIView,
    PurchaseDetailListAPIView,
    PurchaseInvoiceListAPIView,
    PurchaseInvoiceDetailView
)
urlpatterns = [
    path("", PurchaseInvoiceListAPIView.as_view()),
    path("<uuid:pk>/", PurchaseInvoiceDetailView.as_view()),
    path("<uuid:pk>/items/", PurchaseDetailListAPIView.as_view()),
    path("items/<uuid:pk>/", PurchaseDetailAPIView.as_view())
]
