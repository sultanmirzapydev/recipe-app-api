from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

	def test_create_user_with_email_successful(self):
		"""Test creating a new user with an email is successful"""
		email = 'sultanmirza136id@gmail.com'
		password = 'sultanmirza136id'
		user = get_user_model().objects.create_user(
			email = email,
			password = password

		)

		self.assertEqual(user.email, email)
		self.assertTrue(user.check_password(password))

	def test_new_user_email_normalized(self):
		"""Test the email for a new user is normalized"""
		email = 'sultanmirza136id@GMAIL.COM'
		user = get_user_model().objects.create_user(email, 'sultanmirza136id')

		self.assertEqual(user.email, email.lower())


	def test_new_user_invalid_email(self):
		"""Test create user with no email raises error"""
		with self.assertRaises(ValueError):
			get_user_model().objects.create_user(None, 'sultanmirza136id')


	def test_create_new_superuser(self):
		"""Test creating a new superuser"""
		user = get_user_model().objects.create_superuser(
			'sultanmirza136id@gmail.com',
			'sultanmirza136id'

		)

		self.assertTrue(user.is_superuser)
		self.assertTrue(user.is_staff)
		