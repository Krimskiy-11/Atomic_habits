from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from datetime import timedelta

from habits.models import Habit
from users.models import User


class HabitTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="admin@sky.pro"
        )
        self.habit = Habit.objects.create(
            place="Дом",
            time="12:00:00",
            action="Пить больше воды",
            is_pleasant=True,
            period="1",
            time_to_action=timedelta(minutes=1),
            is_published=True,
            owner=self.user
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_habits_create(self):
        url = reverse("habits:habit-list",)
        data = {
        "place": "Дом",
        "time": "11:00:00",
        "action": "Пить больше чая",
        "is_pleasant": True,
        "period": "5",
        "time_to_action": "00:02:00",
        "is_published": True
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Habit.objects.all().count(), 2
        )

    def test_habits_update(self):
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        data = {
            "place": "Улица",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("place"), "Улица"
        )

    def test_habits_retrieve(self):
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("action"), self.habit.action
        )

    def test_habits_list(self):
        url = reverse("habits:habit-list",)
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_habits_delete(self):
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Habit.objects.all().count(), 0
        )
