from django.urls import path
from .views import PharmacyViewSet, MedicineViewSet, OrderViewSet

urlpatterns = [
    path('pharmacy/', PharmacyViewSet.as_view()),
    path('medicine/', MedicineViewSet.as_view()),
    path('orders/', OrderViewSet.as_view(), name='order_create_list'),
]