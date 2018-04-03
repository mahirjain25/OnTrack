from django.test import TestCase, SimpleTestCase

# Create your tests here.


class PagesTests(SimpleTestCase):
	def test_home_page_status_code(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code,200)
	#Test if one cannot view dashboard without logging in
	def test_dash_page_status_code(self):
		response = self.client.get('/accounts/dashboard')
		self.assertEqual(response.status_code,301)
	#Test if one can access admin portal without credentials
	def test_admin_page_status_code(self):
		response = self.client.get('/admin')
		self.assertEqual(response.status_code,301)
		

