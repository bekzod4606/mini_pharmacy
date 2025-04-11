from rest_framework import serializers
from .models import Pharmacy, Medicine, Order

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ['id', 'name', 'city']


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializer(read_only=True)
    medicine_id = serializers.PrimaryKeyRelatedField(queryset=Medicine.objects.all(), write_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only = ('id', 'payment_status', 'created_at')

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError('Quantity must be greater than 0')
        return value

    def create(self, validated_data):
        validated_data['medicine'] = validated_data.pop('medicine_id')
        return super().create(validated_data)