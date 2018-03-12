from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import *

# Create your tests here.
class MessengerPageTest(TestCase):
    def test_inbox_page_resolves(self):
        page = resolve('/messenger/')
        self .assertEqual(page.func, get_inbox)


    def test_sent_page_resolves(self):
        page = resolve('/messenger/sent/')
        self.assertEqual(page.func, sent)
        

    def test_compose_page_resolves(self):
        page = resolve('/messenger/compose_message/')
        self .assertEqual(page.func, compose_message)

        
    def test_view_page_resolves(self):
        page = resolve('/messenger/view_message/1')
        self .assertEqual(page.func, view_message)
        
    def test_message_requires_id(self):
        response = self.client.get('/messenger/view_message/1')
        self .assertEqual(response.status_code, 404)
