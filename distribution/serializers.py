from rest_framework import serializers

from distribution.models import Unit


class UnitSerializer(serializers.ModelSerializer):
    """Сериализатор для модели узла сети"""
    class Meta:
        model = Unit
        fields = '__all__'
        read_only_fields = ['created_at']

    def update(self, instance, validated_data):
        """Нельзя изменять поле Задолженность через API"""
        validated_data.pop('debt', None)
        return super().update(instance, validated_data)
