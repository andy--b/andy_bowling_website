from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()
		self.browser.implicitly_wait(3)

	def test_can_navigate_website(self):
		# Bob from GreatCompany Inc. has heard about this awesome dev
		# and wants to learn about him.
		self.browser.get('http://localhost:8000')

		# He notices the page title and thinks "oh, how appropriate!"
		self.assertIn('Home - Andy Bowling', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('large').text
		self.assertIn('ANDY BOWLING', header_text)
		
		project_link = self.browser.find_element_by_id('proj-button')
		

		# He would like to learn more about Andy's database project.
		# He clicks the link and is brought to a new page
		self.browser.click('proj-button')
		self.assertIn('Project - Andy Bowling', self.browser.title)

		# Satisfied, Bob returns to the home page
		self.fail('Finish the test!')
if __name__ == '__main__':
	unittest.main(warnings='ignore')