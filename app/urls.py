from django.urls import path
from .views import PharmacyViewSet, MedicineViewSet

urlpatterns = [
    path('pharmacy/', PharmacyViewSet.as_view()),
    path('medicine/', MedicineViewSet.as_view()),
]