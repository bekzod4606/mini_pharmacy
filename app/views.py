from rest_framework import generics, filters
from app.models import Pharmacy, Medicine, Order
from .serializers import PharmacySerializer, MedicineSerializer, OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend

class PharmacyViewSet(generics.ListCreateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer

class MedicineViewSet(generics.ListCreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pharmacy', 'in_stock', 'price', 'name']


class OrderViewSet(generics.ListCreateAPIView):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer

    filter_backends = [DjangoFilterBackend ,filters.SearchFilter]
    filterset_fields = ['payment_status', 'medicine']
    search_fields = ['customer_name', 'phone', 'delivery_address']


class OrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'