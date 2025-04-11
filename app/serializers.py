from rest_framework import serializers
from .models import Pharmacy, Medicine, Order

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ['id', 'name', 'city']


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['id', 'name', 'price', 'in_stock', 'pharmacy']


class OrderSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializer(read_only=True)
    medicine_id = serializers.PrimaryKeyRelatedField(queryset=Medicine.objects.all(), write_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'customer_name',
            'phone',
            'medicine',
            'medicine_id',
            'quantity',
            'delivery_address',
            'payment_status',
            'created_at',
        ]
        read_only = ('id', 'payment_status', 'created_at')

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError('Quantity must be greater than 0')
        return value

    def create(self, validated_data):
        validated_data['medicine'] = validated_data.pop('medicine_id')
        return super().create(validated_data)