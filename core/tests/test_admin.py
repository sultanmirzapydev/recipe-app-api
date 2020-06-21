from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

	def setUp(self):
		self.client = Client()
		self.admin_user = get_user_model().objects.create_superuser(
			email = 'sultanmirza136id@gmail.com',
			password = 'sultanmirza136id'

		)
		self.client.force_login(self.admin_user)
		self.user = get_user_model().objects.create_user(
			email = 'sultanmirza136i@gmail.com',
			password = 'sultanmirza136id',
			name = 'Test user full name'
		)

	def test_users_listed(self):
		"""Test that users are listed on user page"""
		url = reverse('admin:core_user_changelist')
		res = self.client.get(url)

		self.assertContains(res, self.user.name)
		self.assertContains(res, self.user.email)

	def test_user_change_page(self):
		"""Test that user edit page works"""
		url = reverse('admin:core_user_change', args=[self.user.id])  # admin/core/user/1   (1 is for user.id)
		res = self.client.get(url)

		self.assertEqual(res.status_code, 200)

	def test_create_user_page(self):
		"""Test that the create user page works"""
		url = reverse('admin:core_user_add')
		res = self.client.get(url)

		self.assertEqual(res.status_code, 200)
