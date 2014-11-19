from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from students_manager.views import student_manager_page, students_page, groups_page
from students_manager.models import Student,Group


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/student_manager/')
        self.assertEqual(found.func, student_manager_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = student_manager_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)


class StudentsPageTest(TestCase):

    def test_students_page_returns_correct_html(self):
        request = HttpRequest()
        response = students_page(request)
        expected_html = render_to_string('students.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_students_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['student_name'] = 'John'
        request.POST['student_last_name_1'] = 'Doe'
        request.POST['student_last_name_2'] = 'Student'

        response = students_page(request)

        self.assertEqual(Student.objects.count(), 1)
        new_student = Student.objects.first()
        self.assertEqual(new_student.name, 'John')
        self.assertEqual(new_student.last_name_1, 'Doe')
        self.assertEqual(new_student.last_name_2, 'Student')

    def test_students_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['student_name'] = 'John'
        request.POST['student_last_name_1'] = 'Doe'
        request.POST['student_last_name_2'] = 'Student'

        response = students_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/student_manager/students/')  # notharcoded

    def test_saving_and_retrieving_students(self):
        first_student = Student()
        first_student.name = 'The first (ever) student'
        first_student.save()

        second_student = Student()
        second_student.name = 'Student the second'
        second_student.save()

        saved_students = Student.objects.all()
        self.assertEqual(saved_students.count(), 2)

        first_saved_student = saved_students[0]
        second_saved_student = saved_students[1]
        self.assertEqual(first_saved_student.name, 'The first (ever) student')
        self.assertEqual(second_saved_student.name, 'Student the second')

    def test_students_page_only_saves_students_when_necessary(self):
        request = HttpRequest()
        students_page(request)
        self.assertEqual(Student.objects.count(), 0)

    def test_students_page_displays_all_list_items(self):
        Student.objects.create(name='student 1')
        Student.objects.create(name='student 2')

        request = HttpRequest()
        response = students_page(request)

        self.assertIn('student 1', response.content.decode())
        self.assertIn('student 2', response.content.decode())


class GroupsPageTest(TestCase):

    def test_groups_page_returns_correct_html(self):
        request = HttpRequest()
        response = groups_page(request)
        expected_html = render_to_string('groups.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_groups_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['group_name'] = 'A new group'

        response = groups_page(request)

        self.assertEqual(Group.objects.count(), 1)
        new_group = Group.objects.first()
        self.assertEqual(new_group.name, 'A new group')

    def test_groups_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['group_name'] = 'A new group'

        response = groups_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/student_manager/groups/')  # notharcoded

    def test_saving_and_retrieving_groups(self):
        first_group = Group()
        first_group.name = 'The first (ever) group'
        first_group.save()

        second_group = Group()
        second_group.name = 'Group the second'
        second_group.save()

        saved_groups = Group.objects.all()
        self.assertEqual(saved_groups.count(), 2)

        first_saved_group = saved_groups[0]
        second_saved_group = saved_groups[1]
        self.assertEqual(first_saved_group.name, 'The first (ever) group')
        self.assertEqual(second_saved_group.name, 'Group the second')

    def test_groups_page_only_saves_groups_when_necessary(self):
        request = HttpRequest()
        groups_page(request)
        self.assertEqual(Group.objects.count(), 0)

    def test_groups_page_displays_all_list_items(self):
        Group.objects.create(name='group 1')
        Group.objects.create(name='group 2')

        request = HttpRequest()
        response = groups_page(request)

        self.assertIn('group 1', response.content.decode())
        self.assertIn('group 2', response.content.decode())