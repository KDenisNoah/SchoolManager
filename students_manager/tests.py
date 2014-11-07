from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from students_manager.views import home_page
from students_manager.models import Student


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['student_text'] = 'A new student'

        response = home_page(request)

        self.assertEqual(Student.objects.count(), 1)
        new_student = Student.objects.first()
        self.assertEqual(new_student.text, 'A new student')

    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['student_text'] = 'A new student'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_saving_and_retrieving_students(self):
        first_student = Student()
        first_student.text = 'The first (ever) student'
        first_student.save()

        second_student = Student()
        second_student.text = 'Student the second'
        second_student.save()

        saved_students = Student.objects.all()
        self.assertEqual(saved_students.count(), 2)

        first_saved_student = saved_students[0]
        second_saved_student = saved_students[1]
        self.assertEqual(first_saved_student.text, 'The first (ever) student')
        self.assertEqual(second_saved_student.text, 'Student the second')

    def test_home_page_only_saves_students_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Student.objects.count(), 0)

    def test_home_page_displays_all_list_items(self):
        Student.objects.create(text='student 1')
        Student.objects.create(text='student 2')

        request = HttpRequest()
        response = home_page(request)

        self.assertIn('student 1', response.content.decode())
        self.assertIn('student 2', response.content.decode())