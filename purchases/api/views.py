from .serializers import (
    PurchaseDetailSerializer,
    PurchaseInvoiceSerializer, 
    PurchaseInvoiceDetailSerializer
)
from purchases.models import (PurchaseDetail, PurchaseInvoice)
from core.mixins import UserMixin

from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.mixins import DestroyModelMixin

class PurchaseInvoiceListAPIView(UserMixin, ListCreateAPIView):
    queryset = PurchaseInvoice.objects.all()
    serializer_class = PurchaseInvoiceSerializer

class PurchaseInvoiceDetailView(DestroyModelMixin, UpdateAPIView):
    queryset = PurchaseInvoice.objects.all()
    serializer_class = PurchaseInvoiceDetailSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class PurchaseDetailListAPIView(ListAPIView):
    serializer_class = PurchaseDetailSerializer

    def get_queryset(self):
        purchase_invoice_id = self.kwargs.get(self.lookup_field)
        return PurchaseDetail.objects.filter(invoice_id = purchase_invoice_id)
    
class PurchaseDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PurchaseDetail.objects.all()
    serializer_class = PurchaseDetailSerializer
