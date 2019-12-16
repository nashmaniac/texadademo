from ..models import Product


class ProductDataLayer(object):
    @classmethod
    def create_product(cls, name) -> Product:
        p = Product(name=name)
        p.save()
        return p

    @classmethod
    def get_product_by_id(cls, id) -> Product:
        return Product.objects.get(id=id)

    @classmethod
    def get_all_products(cls):
        return Product.objects.all()

