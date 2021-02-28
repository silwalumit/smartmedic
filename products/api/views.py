from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,    
)
from .serializers import (ProductSerializer, GenericNameSerializer)
from products.models import (Product, GenericName)
from core.mixins import UserMixin

class ProductListAPIView(UserMixin,ListCreateAPIView):
    page_size_query_param = 'page_size'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class GenericNameListAPIView(UserMixin, ListCreateAPIView):
    queryset = GenericName.objects.all()
    serializer_class = GenericNameSerializer

class GenericNameDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = GenericName.objects.all()
    serializer_class = GenericNameSerializer
