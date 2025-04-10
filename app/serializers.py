from rest_framework import serializers
from .models import Pharmacy, Medicine

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ['id', 'name', 'city']


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'