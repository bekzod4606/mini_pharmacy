from rest_framework import generics
from app.models import Pharmacy, Medicine
from .serializers import PharmacySerializer, MedicineSerializer

class PharmacyViewSet(generics.ListCreateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer

class MedicineViewSet(generics.ListCreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer