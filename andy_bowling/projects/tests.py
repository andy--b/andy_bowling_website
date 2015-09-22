from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from projects.views import home_page, project_page

class SmokeTest(TestCase):
	
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)
		
	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		self.assertTrue(response.content.startswith(b'<!DOCTYPE html>\n<html lang="en">'))
		self.assertIn(b'<title>Home - Andy Bowling</title>', response.content)
		self.assertTrue(response.content.strip().endswith(b'</html>'))
		
	def test_project_url_resolves_to_project_page_view(self):
		found = resolve('/project/')
		self.assertEqual(found.func, project_page)

	def test_project_page_returns_correct_html(self):
		request = HttpRequest()
		response = project_page(request)
		self.assertTrue(response.content.startswith(b'<!DOCTYPE html>\n<html lang="en">'))
		self.assertIn(b'<title>Project - Andy Bowling</title>', response.content)
		self.assertTrue(response.content.strip().endswith(b'</html>'))