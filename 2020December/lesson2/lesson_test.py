import pytest
from datetime import datetime
from .Lesson.lesson import Lesson

lesson1 = Lesson(lesson_name='lesson1',
                 lesson_date='2020-12-21',
                 course_name="Python QA Engineer",
                 module="Introduction",
                 link='')

lesson2 = Lesson(lesson_name='lesson2',
                 lesson_date='2020-12-28',
                 course_name="Python QA Engineer",
                 module="Introduction",
                 link='')


class TestLesson:

    def test_lesson_one(self):
        assert datetime.fromisoformat(lesson1.get_lesson_date()) < \
               datetime.fromisoformat(lesson2.get_lesson_date())

    def test_lesson_two(self):
        """
        TODO: "Проверить что тесты относятся к одному модулю"
        """
