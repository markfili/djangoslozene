"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import datetime
from django.utils import timezone

from dijelovi.models import Part

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class PartMethodTest(TestCase):
	def test_was_published_recently_with_future_part(self):
		future_part = Part(date_added=timezone.now() + datetime.timedelta(days=30))
		self.assertEqual(future_part.was_published_recently(), False)