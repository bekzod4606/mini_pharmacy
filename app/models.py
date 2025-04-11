from django.db import models
from django.core.validators import RegexValidator

class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    in_stock = models.IntegerField()
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)

PHONE_REGEX = RegexValidator(
    regex=r"^\+998([0-9][0-9]|99)\d{7}$",
    message="Please provide a valid phone number.",
)

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(validators=[PHONE_REGEX], max_length=21, unique=False)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    delivery_address = models.TextField()
    payment_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.medicine.name}"
