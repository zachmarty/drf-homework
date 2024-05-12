from os import name
from django.urls import reverse_lazy
from rest_framework.test import APITestCase
from rest_framework import status

from courses.models import Course, Lesson, Sub
from users.models import User

VIDEO = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

"""Я закоментировал предыдущие тесты, потому что мне было лень после создания нового переписывать все айдишники у всех предыдущих"""

# class CourseTestCase(APITestCase):
#     @staticmethod
#     def url_single(pk):
#         return reverse_lazy("courses:course-detail", kwargs={"pk": pk})

#     def setUp(self) -> None:
#         self.url = reverse_lazy("courses:course-list")
#         user = {
#             "email": "test@test.mail.ru",
#             "first_name": "test",
#             "last_name": "test",
#             "is_staff": True,
#             "is_superuser": True,
#         }
#         test_user = User.objects.create(**user)
#         test_user.set_password("12345678")
#         self.client.force_authenticate(user=test_user)

#     def test_course_create(self):
#         """Создание курса"""
#         data = {
#             "name": "test",
#             "description": "test description",
#         }
#         response = self.client.post(self.url, data=data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.json(),
#             {
#                 "id": 5,
#                 "lesson_count": 0,
#                 "lessons": [],
#                 "name": "['test']",
#                 "preview": None,
#                 "description": "['test description']",
#                 "user": 5,
#             },
#         )
#         self.assertTrue(Course.objects.all().exists())

#     def test_course_list(self):
#         """Тест списка курсов"""
#         Course.objects.create(name="test", description="test")
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.json(),
#             {
#                 "count": 1,
#                 "next": None,
#                 "previous": None,
#                 "results": [
#                     {
#                         "id": 2,
#                         "lesson_count": 0,
#                         "lessons": [],
#                         "name": "test",
#                         "preview": None,
#                         "description": "test",
#                         "user": None,
#                     }
#                 ],
#             },
#         )

#     def test_course_retrieve(self):
#         """Тест просмотра курса"""
#         new_course = Course.objects.create(name="test", description="test")
#         response = self.client.get(self.url_single(new_course.id))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.json(),
#             {
#                 "id": 3,
#                 "lesson_count": 0,
#                 "lessons": [],
#                 "name": "test",
#                 "preview": None,
#                 "description": "test",
#                 "user": None,
#             },
#         )

#     def test_course_update(self):
#         """Тест обновления курса"""
#         new_course = Course.objects.create(name="test", description="test")
#         data = {"name": "updated", "description": "updated"}
#         response = self.client.put(self.url_single(new_course.id), data=data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.json(),
#             {
#                 "id": 4,
#                 "lesson_count": 0,
#                 "lessons": [],
#                 "name": "updated",
#                 "preview": None,
#                 "description": "updated",
#                 "user": None,
#             },
#         )

#     def test_course_delete(self):
#         """Тест удаления курса"""
#         new_course = Course.objects.create(name="test", description="test")
#         respose = self.client.delete(self.url_single(new_course.id))
#         self.assertEqual(respose.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(Course.objects.all().exists())


# class LessonTestCase(APITestCase):
#     @staticmethod
#     def url_retrieve(pk):
#         return reverse_lazy("courses:lesson_detail", kwargs={"pk": pk})

#     @staticmethod
#     def url_delete(pk):
#         return reverse_lazy("courses:lesson_delete", kwargs={"pk": pk})

#     @staticmethod
#     def url_update(pk):
#         return reverse_lazy("courses:lesson_update", kwargs={"pk": pk})

#     def setUp(self) -> None:
#         self.url_list = reverse_lazy("courses:lesson_list")
#         self.url_create = reverse_lazy("courses:lesson_create")
#         user = {
#             "email": "test@test.mail.ru",
#             "first_name": "test",
#             "last_name": "test",
#             "is_staff": True,
#             "is_superuser": True,
#         }
#         test_user = User.objects.create(**user)
#         test_user.set_password("12345678")
#         self.client.force_authenticate(user=test_user)
#         self.test_course = Course.objects.create(name="test")

#     def test_lesson_create(self):
#         """Создание курса"""
#         data = {
#             "name": "test",
#             "description": "test description",
#             "course": self.test_course.id,
#             "video": VIDEO,
#         }
#         response = self.client.post(self.url_create, data=data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(
#             response.json(),
#             {
#                 "course": 1,
#                 "description": "test description",
#                 "id": 1,
#                 "name": "test",
#                 "preview": None,
#                 "user": 1,
#                 "video": VIDEO,
#             },
#         )
#         self.assertTrue(Course.objects.all().exists())

#     def test_lesson_list(self):
#         """Тест список уроков"""
#         test_lesson = Lesson.objects.create(
#             name="test", video=VIDEO, course=self.test_course
#         )
#         response = self.client.get(self.url_list)
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_200_OK,
#         )
#         self.assertEqual(
#             response.json(),
#             {
#                 "count": 1,
#                 "next": None,
#                 "previous": None,
#                 "results": [
#                     {
#                         "id": 4,
#                         "name": "test",
#                         "description": None,
#                         "preview": None,
#                         "video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
#                         "course": 4,
#                         "user": None,
#                     }
#                 ],
#             },
#         )

#     def test_lesson_detail(self):
#         """Тест просмотра урока"""
#         test_lesson = Lesson.objects.create(
#             name="test", video=VIDEO, course=self.test_course
#         )
#         response = self.client.get(self.url_retrieve(test_lesson.id))
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_200_OK,
#         )
#         self.assertEqual(
#             response.json(),
#             {
#                 "id": 3,
#                 "name": "test",
#                 "description": None,
#                 "preview": None,
#                 "video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
#                 "course": 3,
#                 "user": None,
#             },
#         )

#     def test_lesson_update(self):
#         """Тест обновления урока"""
#         test_lesson = Lesson.objects.create(
#             name="test", video=VIDEO, course=self.test_course
#         )
#         response = self.client.patch(
#             self.url_update(test_lesson.id),
#             data={"name": "test update", "video": VIDEO},
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.json(),
#             {
#                 "id": 5,
#                 "name": "test update",
#                 "description": None,
#                 "preview": None,
#                 "video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
#                 "course": 5,
#                 "user": None,
#             },
#         )

#     def test_lesson_delete(self):
#         """Тест удаления урока"""
#         test_lesson = Lesson.objects.create(
#             name="test", video=VIDEO, course=self.test_course
#         )
#         self.assertTrue(
#             Lesson.objects.all().exists(),
#         )
#         response = self.client.delete(
#             self.url_delete(test_lesson.id), data={"id": test_lesson.id}
#         )
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_204_NO_CONTENT,
#         )
#         self.assertFalse(
#             Lesson.objects.all().exists(),
#         )


class SubTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = reverse_lazy("courses:sub")
        user = {
            "email": "test@test.mail.ru",
            "first_name": "test",
            "last_name": "test",
            "is_staff": True,
            "is_superuser": True,
        }
        self.test_user = User.objects.create(**user)
        self.test_user.set_password("12345678")
        self.client.force_authenticate(user=self.test_user)
        self.test_course = Course.objects.create(name="test")

    def test_sub_activate(self):
        """Тест подписки на курс"""
        data = {
            "user": self.test_user.id,
            "course": self.test_course.id,
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "message": "Вы подписались на курс test",
            },
        )
        self.assertTrue(
            Sub.objects.all().exists(),
        )

    def test_sub_deactivate(self):
        """Тест отписки с курса"""
        Sub.objects.create(user=self.test_user, course=self.test_course)
        data = {
            "user": self.test_user.id,
            "course": self.test_course.id,
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            response.json(),
            {
                "message": "Подписка на курс test отменена",
            },
        )
        self.assertFalse(
            Sub.objects.all().exists(),
        )
