class Lesson:

    def __init__(self, link, lesson_date, course_name, lesson_name, module):
        self.link = link
        self.lesson_date = lesson_date
        self.course_name = course_name
        self.lesson_name = lesson_name
        self.module = module

    def get_module(self):
        return self.module

    def get_course_name(self):
        return self.course_name

    def get_lesson_date(self):
        return self.lesson_date
