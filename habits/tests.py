import time

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@admin.com")
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            owner=self.user,
            time="22:00",
            action="run",
        )

    def test_habit_retrieve(self):
        url = reverse("habits:habit-retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("action"), self.habit.action
        )

    def test_habit_list(self):
        url = reverse("habits:habit-list")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            Habit.objects.all().count(), 1
        )
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "owner": self.user.pk,
                    "location": None,
                    "time": self.habit.time + ":00",
                    "action": self.habit.action,
                    "is_pleasant_habit": False,
                    "related_habit": None,
                    "periodicity": 1,
                    "award": None,
                    "time_complete": 1,
                    "is_publication": False,
                }
            ]
        }
        self.assertEqual(
            data, result
        )
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_habit_create(self):
        url = reverse("habits:habit-create")
        data = {
            "owner": self.user.pk,
            "time": "23:00",
            "action": "run 2"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            Habit.objects.all().count(), 2
        )
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

    def test_habit_update(self):
        url = reverse("habits:habit-update", args=(self.habit.pk,))
        data = {
            "time": "21:00",
            "action": "sleep"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            data.get("action"), "sleep"
        )
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )