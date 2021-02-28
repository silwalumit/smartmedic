from django.urls import path
from .views import (
    DistributorListAPIView, 
    DistributorDetailAPIView,
    ManufacturerListAPIView,
    ManufacturerDetailAPIView,
    CustomerListAPIView,
)
urlpatterns = [
    path("manufacturers/", ManufacturerListAPIView.as_view()),
    path("manufacturers/<uuid:pk>/", ManufacturerDetailAPIView.as_view()),
    path("distributors/", DistributorListAPIView.as_view()),
    path("distributors/<uuid:pk>/", DistributorDetailAPIView.as_view()),
    path("customers/", CustomerListAPIView.as_view()),
]
