from rest_framework.test import APITestCase
from rest_framework import status

class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        return super().setUp()
    
    def test_create_course(self):
        """
        Создание курса
        """
        data = {
            "name":"test",
            "description":"test description",

        }
        response = self.client.put(
            'course/create/',
            data=data
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        return super().setUp()
    
    def test_create_lesson(self):
        """
        Создание урока
        """
        data = {
            "name":"test",
            "description":"test description",
            "course":1
        }
        request_data = {
            'content_type': 'application/json',
        } 

        request_data.update(headers_to_send)
        request_data['data'] = data
        response = self.client.post(
            'lesson/create',
            **request_data
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
