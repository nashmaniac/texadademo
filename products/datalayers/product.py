from ..models import Product, Tracking


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

    @classmethod
    def create_tracking(cls, data) -> Tracking:
        p = Product.objects.get(id=data.get('product'))
        t = Tracking(
            product=p, timestamp=data.get('timestamp'),
            latitude=data.get('latitude'), longitude=data.get('longitude'),
            elevation=data.get('elevation')
        )
        t.save()
        return t


    @classmethod
    def get_tracking_by_id(cls, id) -> Tracking:
        return Tracking.objects.prefetch_related('product').get(id=id)

    @classmethod
    def get_all_tracking(cls):
        return Tracking.objects.prefetch_related('product').all()

    @classmethod
    def edit_tracking(cls, id, data):
        p = cls.get_tracking_by_id(id)
        product = cls.get_product_by_id(data.get('product'))
        p.product = product
        p.timestamp = data.get('timestamp')
        p.latitude = data.get('latitude')
        p.longitude = data.get('longitude')
        p.elevation = data.get('elevation')
        p.save()
        return p

    @classmethod
    def edit_product(cls, id, data):
        p = cls.get_product_by_id(id)
        p.name = data.get('name')
        p.save()
        return p
