from django.test import TestCase
from home.views import get_index
from django.core.urlresolvers import resolve
from django.test import TestCase
from .views import *

# Create your tests here.

class HomePageTest(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self .assertEqual(home_page.func, get_index)

    def test_index_template_is_correct(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, "home/index.html")