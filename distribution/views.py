from django_filters.rest_framework import DjangoFilterBackend

from distribution.models import Unit
from rest_framework import generics


from distribution.serializers import UnitSerializer
from users.permissions import IsActive


class UnitListAPIView(generics.ListAPIView):
    """Список филиалов"""
    serializer_class = UnitSerializer
    permission_classes = [IsActive]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city']


class UnitRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра данных о филиале"""
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsActive]


class UnitCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания привычек"""
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def perform_create(self, serializer):
        unit = serializer.save()
        if unit.supplier:
            supplier_level = unit.supplier.level
            if supplier_level == 2:
                unit.level = 2
            else:
                unit.level = supplier_level + 1

        else:
            unit.level = 0
        unit.save()


class UnitUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для обновления привычек"""
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsActive]

    def perform_update(self, serializer):
        unit = serializer.save()
        if unit.supplier:
            supplier_level = unit.supplier.level
            if supplier_level == 2:
                unit.level = 2
            unit.level = supplier_level + 1

        else:
            unit.level = 0
        unit.save()


class UnitDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления привычек"""
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsActive]
