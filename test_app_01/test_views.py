import json
from django.test import TestCase
from django.urls import reverse


# Test JsonResponse
class JsonResponseTest(TestCase):
    def test_response(self):
        response = self.client.get(reverse('test_json_response'))
        print('response:', response)

        self.assertEqual(response.status_code, 200)

        json_object = json.loads(response.content)
        print(json.dumps(json_object, indent=4, sort_keys=True))
        self.assertEqual(json_object['ok'], True)


# Test HttpResponse
class HttpResponseTest(TestCase):
    def test_response(self):
        response = self.client.get(reverse('test_page'))
        print('response:', response)

        self.assertEqual(response.status_code, 200)

        print('response.content: ', response.content)


# Test render a template view
class RenderTemplateTest(TestCase):
    def test_response(self):
        response = self.client.get(reverse('test_template'))
        print('response:', response)

        self.assertEqual(response.status_code, 200)


# Test render a table view
class RenderTableTest(TestCase):
    def test_response(self):
        response = self.client.get(reverse('table_template'))
        print('response:', response)

        self.assertEqual(response.status_code, 200)


# Test render a barchart view
class RenderBarchartTest(TestCase):
    def test_response(self):
        response = self.client.get(reverse('barchart_view'))
        print('response:', response)

        self.assertEqual(response.status_code, 200)
