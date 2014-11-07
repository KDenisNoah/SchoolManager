from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # She notices the page title and header mention students manager
        assert 'Students' in self.browser.title, "Browser title was " + self.browser.title

        # She is invited to enter a student straight away

        # She types "Piotr ugrumov" into a text box

        # When she hits enter, the page updates, and now the page lists
        # "Piotr Ugrumov" as a student

        # There is still a text box inviting her to add another student. She
        # enters "Eddy Seigneur"

        # The page updates again, and now shows both students on her list

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her students still there.

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main()