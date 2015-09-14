from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
		self.browser.implicitly_wait(3)

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Bob from GreatCompany Inc. has heard about this awesome dev
		# and wants to learn about him.
        self.browser.get('http://localhost:8000')

        # He notices the page title and thinks "oh, how appropriate!"
        self.assertIn('Home - Andy Bowling', self.browser.title)
        self.fail('Finish the test!')

        # He would like to learn more about Andy's database project.
		# He clicks the link and is brought to a new page
		
		# Satisfied, Bob returns to the home page

if __name__ == '__main__':
    unittest.main(warnings='ignore')