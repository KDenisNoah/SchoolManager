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

    def test_can_start_a_students_list_and_retrieve_it_later(self):
        # Edith headmaster has heard about a cool new online student management
        # She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention student manager
        self.assertIn('Students Manager', self.browser.title)

        #There is a link to /students page
        students_url = self.browser.find_element_by_link_text('Students').get_attribute('href')
        self.assertIn('students', students_url)
        self.browser.get(students_url)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Students', header_text)

        # She is invited to enter a student straight away
        inputbox = self.browser.find_element_by_id('id_new_student')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a student'
        )

        # She types "Piotr Ugrumov" into a text box
        inputbox.send_keys('Piotr Ugrumov')

        # When she hits enter, the page updates, and now the page lists
        # "Piotr Ugrumov" as an item in a student list table
        inputbox.send_keys(Keys.ENTER)
        import time
        time.sleep(2)
        self.check_for_row_in_list_table('Piotr Ugrumov')

        # There is still a text box inviting her to add another student. She
        # enters "Eddie Seigneur"
        inputbox = self.browser.find_element_by_id('id_new_student')
        inputbox.send_keys('Eddie Seigneur')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('Piotr Ugrumov')
        self.check_for_row_in_list_table('Eddie Seigneur')

        self.fail('Finish the test!')

    def test_can_start_a_groups_list_and_retrieve_it_later(self):
        # Edith headmaster has heard about a cool new online student management
        # She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention student manager
        self.assertIn('Students Manager', self.browser.title)

        #There is a link to /group page
        groups_url = self.browser.find_element_by_link_text('Groups').get_attribute('href')
        self.assertIn('groups', groups_url)
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


if __name__ == '__main__':
    unittest.main()