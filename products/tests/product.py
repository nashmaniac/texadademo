from django.test import TestCase, Client
from ..datalayers import ProductDataLayer
from ..models import Product
from django.urls import reverse, reverse_lazy


# Create your tests here.
class ProductTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.name = 'test_data'

    def test_create_product(self):
        p = ProductDataLayer.create_product(self.name)
        assert (isinstance(p, Product))
        assert (isinstance(p.id, int))
        assert (p.name == self.name)

    def test_get_product_by_id(self):
        p = ProductDataLayer.create_product(self.name)
        id = p.id
        product_from_db = ProductDataLayer.get_product_by_id(id)
        assert (p.id == product_from_db.id)
        assert (p.name == product_from_db.name)


class ProductTestCaseWithServer(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        url = reverse('products:api:v1:product_api_view')
        detail_url = reverse('products:api:v1:product_detail_api_view', args=[1, ])
        cls.create_response = cls.client.post(url, data=dict(name='test_product'))
        cls.get_response = cls.client.get(detail_url)
        cls.list_response = cls.client.get(url)

    def test_create_product(self):
        self.assertEqual(self.create_response.status_code, 200)
        assert (isinstance(self.create_response.data, dict))

    def test_get_product_detail(self):
        self.assertEqual(self.get_response.status_code, 200)
        assert (isinstance(self.get_response.data, dict))

    def test_get_product_list(self):
        self.assertEqual(self.list_response.status_code, 200)
        self.assertIsInstance(self.list_response.data, dict)
        self.assertIn('data', self.list_response.data)
        self.assertIn('page', self.list_response.data)
        self.assertIn('limit', self.list_response.data)
        self.assertIn('count', self.list_response.data)


