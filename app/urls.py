from django.urls import path
from app.views import PharmacyViewSet, MedicineViewSet, OrderViewSet, OrderRetrieveUpdateDestroy

urlpatterns = [
    path('pharmacies/', PharmacyViewSet.as_view(), name='pharmacies'),
    path('medicines/', MedicineViewSet.as_view(), name='medicines'),
    path('orders/', OrderViewSet.as_view(), name='orders'),
    path('orders/<int:id>/', OrderRetrieveUpdateDestroy.as_view(), name='order-details'),
]
