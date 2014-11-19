from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from school_qms.views import qms_page, processes_page, procedures_page
from school_qms.models import Process, Procedure


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/qms/')
        self.assertEqual(found.func, qms_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = qms_page(request)
        expected_html = render_to_string('qms_home.html')
        self.assertEqual(response.content.decode(), expected_html)


class ProcessPageTest(TestCase):

    def test_processes_page_returns_correct_html(self):
        request = HttpRequest()
        response = processes_page(request)
        expected_html = render_to_string('processes.html')
        self.assertEqual(response.content.decode(), expected_html)


    def test_process_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['process_name'] = 'A new process'

        response = processes_page(request)

        self.assertEqual(Process.objects.count(), 1)
        new_process = Process.objects.first()
        self.assertEqual(new_process.name, 'A new process')

    def test_process_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['process_name'] = 'A new process'

        response = processes_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/qms/processes/')  # notharcoded

    def test_saving_and_retrieving_processes(self):
        first_process = Process()
        first_process.name = 'The first (ever) process'
        first_process.save()

        second_process = Process()
        second_process.name = 'Process the second'
        second_process.save()

        saved_process = Process.objects.all()
        self.assertEqual(saved_process.count(), 2)

        first_saved_process = saved_process[0]
        second_saved_process = saved_process[1]
        self.assertEqual(first_saved_process.name, 'The first (ever) process')
        self.assertEqual(second_saved_process.name, 'Process the second')

    def test_processs_page_only_saves_processs_when_necessary(self):
        request = HttpRequest()
        processes_page(request)
        self.assertEqual(Process.objects.count(), 0)

    def test_processs_page_displays_all_list_items(self):
        Process.objects.create(name='process 1', description='process 1')
        Process.objects.create(name='process 2', description='process 2')

        request = HttpRequest()
        response = processes_page(request)

        self.assertIn('process 1', response.content.decode())
        self.assertIn('process 2', response.content.decode())


class ProcedurePageTest(TestCase):

    def test_students_page_returns_correct_html(self):
        request = HttpRequest()
        response = procedures_page(request)
        expected_html = render_to_string('procedures.html')
        self.assertEqual(response.content.decode(), expected_html)


    def test_procedure_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['procedure_name'] = 'A new procedure'

        response = procedures_page(request)

        self.assertEqual(Procedure.objects.count(), 1)
        new_procedure = Procedure.objects.first()
        self.assertEqual(new_procedure.name, 'A new procedure')

    def test_procedure_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['procedure_name'] = 'A new procedure'

        response = procedures_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/qms/procedures/')  # notharcoded

    def test_saving_and_retrieving_procedures(self):
        first_procedure = Procedure()
        first_procedure.name = 'The first (ever) procedure'
        first_procedure.save()

        second_procedure = Procedure()
        second_procedure.name = 'Procedure the second'
        second_procedure.save()

        saved_procedure = Procedure.objects.all()
        self.assertEqual(saved_procedure.count(), 2)

        first_saved_procedure = saved_procedure[0]
        second_saved_procedure = saved_procedure[1]
        self.assertEqual(first_saved_procedure.name, 'The first (ever) procedure')
        self.assertEqual(second_saved_procedure.name, 'Procedure the second')

    def test_procedures_page_only_saves_procedures_when_necessary(self):
        request = HttpRequest()
        procedures_page(request)
        self.assertEqual(Procedure.objects.count(), 0)

    def test_procedures_page_displays_all_list_items(self):
        Procedure.objects.create(name='procedure 1', description='procedure 1')
        Procedure.objects.create(name='procedure 2', description='procedure 2')

        request = HttpRequest()
        response = procedures_page(request)

        self.assertIn('procedure 1', response.content.decode())
        self.assertIn('procedure 2', response.content.decode())