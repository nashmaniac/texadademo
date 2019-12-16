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
    def setUp(self) -> None:
        self.client = Client()

    def test_create_product(self):
        url = reverse_lazy('products:api:v1:product_api_view')
        response = self.client.post(url, data=dict(name='test_product'))
        self.assertEqual(response.status_code, 200)
        assert (isinstance(response.data, dict))
