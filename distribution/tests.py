from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from distribution.models import Unit
from distribution.serializers import UnitSerializer
from users.models import User


class UnitSerializerTest(TestCase):
    """Тест сериализатора для модели филиала"""

    def test_supplier_serialization(self):
        unit = Unit.objects.create(
            name='Филиал A',
            email='test@test.com',
            debt=1500.15,
            country='Россия',
            city='Тест',
            street='Тестовая',
            house_number='8',
            level=0
        )

        serializer = UnitSerializer(unit)
        data = serializer.data

        # Проверка сериализованных данных
        self.assertEqual(data['name'], unit.name)
        self.assertEqual(data['debt'], str(unit.debt))
        self.assertEqual(data['email'], unit.email)
        self.assertEqual(data['level'], unit.level)


class UnitAPITestCase(APITestCase):
    """Тесты API для работы с моделью филиала"""

    def setUp(self):
        self.user = User.objects.create(username='test', email='testuser@test.com', password='testpass')
        self.client.force_authenticate(user=self.user)

        self.unit1 = Unit.objects.create(
            name='Филиал 1',
            email='test1@test.com',
            debt=1500.15,
            country='Россия',
            city='Тест',
            street='Тестовая',
            house_number='8',
            level=0
        )
        self.unit2 = Unit.objects.create(
            name='Филиал 2',
            email='test2@test.com',
            debt=150.50,
            country='Россия',
            city='Тест',
            street='Тестовая',
            house_number='5',
            supplier=self.unit1,
            level=1
        )

    def test_unit_retrieve_api(self):
        """Тест получения информации об отдельном филиале"""
        url = reverse('distribution:unit-get', args=[self.unit1.pk])  # Убедитесь, что у вас правильно настроен маршрут
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], self.unit1.name)

    def test_unit_create(self):
        """Тест создания нового филиала"""
        self.client.login(email='testuser@test.com', password='testpass')

        url = reverse('distribution:unit-create')
        data = {
            'name': 'Филиал 3',
            'email': 'test3@test.com',
            'debt': 0.00,
            'country': 'Россия',
            'city': 'Тест',
            'street': 'Тестовая',
            'house_number': '1',
            'level': '2',
            'supplier': self.unit2.pk

        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Unit.objects.all().count(), 3
        )
        test_unit = Unit.objects.get(pk=3)
        self.assertEqual(
            test_unit.level, 2
        )
        self.assertEqual(
            test_unit.city, 'Тест'
        )

    def test_unit_update(self):
        """Тест обновления информации о фиилиале с проверкой сохранения долга"""
        url = reverse('distribution:unit-update', args=(self.unit2.pk,))
        data = {
            'name': 'Филиал 4',
            'country': 'Болгария',
            'debt': 500000.00
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), 'Филиал 4'
        )
        self.assertEqual(
            data.get('country'), 'Болгария'
        )
        self.assertEqual(
            data.get('debt'), '150.50'  # Долг не должен измениться
        )

    def test_unit_delete(self):
        """Тест удаления филиала"""
        url = reverse('distribution:unit-delete', args=(self.unit2.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Unit.objects.all().count(), 1
        )
        self.assertFalse(
            Unit.objects.filter(pk=self.unit2.pk).exists()
        )
