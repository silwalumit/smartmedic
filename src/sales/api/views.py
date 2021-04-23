from sales.models import SalesInvoice, Sales
from .serializers import SalesInvoiceSerializer, SalesSerializer
from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,

)

from core.mixins import UserMixin

class SalesInvoiceListAPIView(UserMixin, ListCreateAPIView):
    queryset = SalesInvoice.objects.all()
    serializer_class = SalesInvoiceSerializer 

