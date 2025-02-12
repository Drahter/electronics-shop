from django.urls import path

from distribution.apps import DistributionConfig
from distribution.views import (
    UnitCreateAPIView,
    UnitListAPIView,
    UnitUpdateAPIView,
    UnitDestroyAPIView,
    UnitRetrieveAPIView
)

app_name = DistributionConfig.name

urlpatterns = [
    path('units/create/', UnitCreateAPIView.as_view(), name='unit-create'),
    path('units/', UnitListAPIView.as_view(), name='unit-list'),
    path('units/update/<int:pk>/', UnitUpdateAPIView.as_view(), name='unit-update'),
    path('units/delete/<int:pk>/', UnitDestroyAPIView.as_view(), name='unit-delete'),
    path('units/<int:pk>/', UnitRetrieveAPIView.as_view(), name='unit-get'),
]
