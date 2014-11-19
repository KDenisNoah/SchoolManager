from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def get_user_id_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        for row in rows:
            if row_text in row:
                print(row_text)

    def test_can_start_a_students_list_and_retrieve_it_later(self):
        # Edith headmaster has heard about a cool new online student management
        # She goes to check out its homepage
        self.browser.get('http://localhost:8000/student_manager')

        # She notices the page title and header mention student manager
        self.assertIn('Students Manager', self.browser.title)

        #There is a link to /students page
        students_url = self.browser.find_element_by_link_text('Students').get_attribute('href')
        self.assertIn('students', students_url)  # hardcoded url?
        self.browser.get(students_url)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Students', header_text)

        # She is invited to enter a student straight away
        name_inputbox = self.browser.find_element_by_id('id_first_name')
        self.assertEqual(
                name_inputbox.get_attribute('placeholder'),
                'First name'
        )
        # She types "Piotr" into a text box
        name_inputbox.send_keys('Piotr')
        last_name_1_inputbox = self.browser.find_element_by_id('id_last_name_1')
        last_name_1_inputbox.send_keys('Ugrumov')
        last_name_2_inputbox = self.browser.find_element_by_id('id_last_name_2')
        last_name_2_inputbox.send_keys('Argentin')
        picture = self.browser.find_element_by_name("id_picture")
        picture.send_keys("/home/asier/Deskargak/picture.png")

        # When she hits enter, the page updates, and now the page lists
        # "Ugrumov Argentin, Piotr" as an item in a student list table
        button = self.browser.find_element_by_id('add_student')
        button.send_keys(Keys.ENTER)
        import time
        time.sleep(2)
        self.check_for_row_in_list_table('Ugrumov Argentin, Piotr')

        image = self.browser.find_element_by_tag_name("img")
        self.assertIn(self.get_user_id_in_list_table('Ugrumov Argentin, Piotr'),image.get_attribute("src"))
        self.fail('Test image upload!')

        # There is still a text box inviting her to add another student. She
        # enters "Eddie Seigneur"
        name_inputbox = self.browser.find_element_by_id('id_first_name')
        name_inputbox.send_keys('Eddie')
        last_name_1_inputbox = self.browser.find_element_by_id('id_last_name_1')
        last_name_1_inputbox.send_keys('Seigneur')
        last_name_2_inputbox = self.browser.find_element_by_id('id_last_name_2')
        last_name_2_inputbox.send_keys('Virenque')
        picture = self.browser.find_element_by_name("id_picture")
        picture.send_keys("/home/asier/Deskargak/picture.png")
        button = self.browser.find_element_by_id('add_student')
        button.send_keys(Keys.ENTER)

        self.fail('Test image upload!')

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('Ugrumov Argentin, Piotr')
        self.check_for_row_in_list_table('Seigneur Virenque, Eddie')

        self.fail('Finish the test!')

    def test_can_start_a_groups_list_and_retrieve_it_later(self):
        # Edith headmaster has heard about a cool new online student management
        # She goes to check out its homepage
        self.browser.get('http://localhost:8000/student_manager')

        # She notices the page title and header mention student manager
        self.assertIn('Students Manager', self.browser.title)

        #There is a link to /group page
        groups_url = self.browser.find_element_by_link_text('Groups').get_attribute('href')
        self.assertIn('groups', groups_url)  # hardcoded url?
        self.browser.get(groups_url)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Groups', header_text)

        # She is invited to enter a group straight away
        inputbox = self.browser.find_element_by_id('id_new_group')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a group'
        )

        # She types "1A" into a text box
        inputbox.send_keys('1A')

        # When she hits enter, the page updates, and now the page lists
        # "1A" as an item in a group list table
        inputbox.send_keys(Keys.ENTER)
        import time
        time.sleep(2)
        self.check_for_row_in_list_table('1A')

        # There is still a text box inviting her to add another group. She
        # enters "2C"
        inputbox = self.browser.find_element_by_id('id_new_group')
        inputbox.send_keys('2C')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1A')
        self.check_for_row_in_list_table('2C')

        self.fail('Finish the test!')

    def test_can_start_a_process_list_and_retrieve_it_later(self):
        # Edith headmaster has heard about a cool new online school QMS
        # She goes to check out its homepage
        self.browser.get('http://localhost:8000/qms')

        # She notices the page title and header mention School QMS
        self.assertIn('School QMS', self.browser.title)

        #There is a link to /processes page
        processes_url = self.browser.find_element_by_link_text('Processes').get_attribute('href')
        self.assertIn('processes', processes_url)  # hardcoded url?
        self.browser.get(processes_url)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Processes', header_text)

        # She is invited to enter a process name straight away
        inputbox = self.browser.find_element_by_id('id_new_process')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a process'
        )

        # She types "PR0101" into a text box
        inputbox.send_keys('PR0101')

        # When she hits enter, the page updates, and now the page lists
        # "PR0101" as an item in a processes list table
        inputbox.send_keys(Keys.ENTER)
        import time
        time.sleep(2)
        self.check_for_row_in_list_table('PR0101')

        # There is still a text box inviting her to add another process. She
        # enters "PR0102"
        inputbox = self.browser.find_element_by_id('id_new_process')
        inputbox.send_keys('PR0102')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('PR0101')
        self.check_for_row_in_list_table('PR0102')

        self.fail('Finish the test!')

    def test_can_start_a_procedure_list_and_retrieve_it_later(self):
        # Edith headmaster has heard about a cool new online school QMS
        # She goes to check out its homepage
        self.browser.get('http://localhost:8000/qms')

        # She notices the page title and header mention School QMS
        self.assertIn('School QMS', self.browser.title)

        #There is a link to /procedures page
        procedures_url = self.browser.find_element_by_link_text('Procedures').get_attribute('href')
        self.assertIn('procedures', procedures_url)  # hardcoded url?
        self.browser.get(procedures_url)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Procedures', header_text)

        # She is invited to enter a procedure name straight away
        inputbox = self.browser.find_element_by_id('id_new_procedure')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a procedure'
        )

        # She types "PR0101" into a text box
        inputbox.send_keys('PR0101')

        # When she hits enter, the page updates, and now the page lists
        # "PR0101" as an item in a procedures list table
        inputbox.send_keys(Keys.ENTER)
        import time
        time.sleep(2)
        self.check_for_row_in_list_table('PR0101')

        # There is still a text box inviting her to add another procedure. She
        # enters "PR0102"
        inputbox = self.browser.find_element_by_id('id_new_procedure')
        inputbox.send_keys('PR0102')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('PR0101')
        self.check_for_row_in_list_table('PR0102')

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
#    unittest.main()