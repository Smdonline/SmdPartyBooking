"""Tests for models"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models"""
    def test_create_user_with_email_successful(self):
        """Test creating a user with email is successful"""
        email = "user@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password), msg="invalid password")

    def test_new_user_email_normalised(self):
        """Test if email is normalised"""
        sample_email = [
            ['user@EXAMPLE.com', 'user@example.com'],
            ['User1@Example.com', 'User1@example.com'],
            ['user2@EXAMPLE.COM', 'user2@example.com'],
            ['user3@example.COM', 'user3@example.com'],
        ]
        for email, expected in sample_email:
            user = get_user_model().objects.create_user(
                email=email,
                password="test1345!!"
            )

            self.assertEquals(user.email, expected)

    def test_new_user_with_empty_email(self):
        """Test if raise an error if email is empty"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email='',
                password="test123!!"
            )

    def test_create_superuser(self):
        """Test if superuser is created"""
        user = get_user_model().objects.create_superuser(
            email="test1@example.com",
            password="test123!"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
