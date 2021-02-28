from .serializers import (
    DistributorSerializer, 
    ManufacturerSerializer, 
    CustomerSerializer
)

from rest_framework.generics import (
    ListCreateAPIView,RetrieveUpdateDestroyAPIView
    
)
from contacts.models import Distributor, Manufacturer, Customer
from core.mixins import UserMixin

class DistributorListAPIView(UserMixin, ListCreateAPIView):
    permission_classes = []
    serializer_class = DistributorSerializer
    queryset = Distributor.objects.all()

class DistributorDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class = DistributorSerializer
    queryset = Distributor.objects.all()

class ManufacturerListAPIView(UserMixin, ListCreateAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()

class ManufacturerDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class CustomerListAPIView(UserMixin, ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
