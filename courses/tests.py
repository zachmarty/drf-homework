from django.urls import reverse_lazy
from rest_framework.test import APITestCase
from rest_framework import status

from users.models import User


class CourseCreateTestCase(APITestCase):
    url = reverse_lazy("courses:course-list")

    def setUp(self) -> None:
        return super().setUp()

    def test_create_course_by_anonymous(self):
        """
        Создание курса
        """
        data = {
            "name": "test",
            "description": "test description",
        }
        test_admin = User.objects.create(
            email="admin@mail.ru",
            first_name="admin",
            last_name="admin",
            is_staff=True,
            is_superuser=True,
        )
        test_admin.set_password("12345678")
        self.client.force_login(user=test_admin)
        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test_create_lesson(self):
        """
        Создание урока
        """
        data = {"name": "test", "description": "test description", "course": 1}
        request_data = {
            "content_type": "application/json",
        }
        # self.client.credentials(**headers)
        request_data["data"] = data
        response = self.client.post("lesson/create", **request_data)
        print(response.text)

        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
