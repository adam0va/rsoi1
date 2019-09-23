from django.test import TestCase
from people.models import Person
from rest_framework.test import APIClient
from django.test.runner import DiscoverRunner

class NoDbTestRunner(DiscoverRunner):

    def setup_databases(self, **kwargs):
        """ Override the database creation defined in parent class """
        pass

    def teardown_databases(self, old_config, **kwargs):
        """ Override the database teardown defined in parent class """
        pass

class PeopleTestCase(TestCase):
    def setUp(self):
         self.client = APIClient()
    def test_get(self):
        result = self.client.get('/people/')
        self.assertNotEqual(len(result.json()), 0)

# Create your tests here.
