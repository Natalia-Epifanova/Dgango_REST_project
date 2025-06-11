from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from materials.models import Course
from users.models import User, Subscription


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="user@mail.com")
        self.course = Course.objects.create(name="Курс с подпиской")
        self.client.force_authenticate(user=self.user)

    def test_subscribe_to_course(self):
        """Проверка подписки на курс"""
        url = reverse("users:subscriptions")
        data = {"course_id": self.course.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(
            Subscription.objects.filter(user=self.user, course=self.course).exists()
        )
        self.assertIn("Подписка добавлена", response.data["message"])

    def test_unsubscribe_from_course(self):
        """Проверка отписки от курса"""
        Subscription.objects.create(user=self.user, course=self.course)

        url = reverse("users:subscriptions")
        data = {"course_id": self.course.pk}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(
            Subscription.objects.filter(user=self.user, course=self.course).exists()
        )
        self.assertIn("Подписка удалена", response.data["message"])

    def test_subscription_without_course_id(self):
        """Проверка обработки запроса без course_id"""
        url = reverse("users:subscriptions")
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"], "course_id is required")
        self.assertEqual(Subscription.objects.count(), 0)
