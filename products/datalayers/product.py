from ..models import Product, Tracking
import datetime, pytz


class ProductDataLayer(object):
    @classmethod
    def create_product(cls, name) -> Product:
        '''
        create product factory function
        '''
        p = Product(name=name)
        p.save()
        return p

    @classmethod
    def get_product_by_id(cls, id) -> Product:
        '''
        get product by product id
        '''
        return Product.objects.get(id=id)

    @classmethod
    def get_all_products(cls):
        '''
        return all product objects
        '''
        return Product.objects.all()

    @classmethod
    def filter_product_queryset_by_text(cls, queryset, search_term):
        '''
        case insensitive text filtering in name field of product queryset
        '''
        if search_term:
            return queryset.filter(name__icontains=search_term)
        return queryset

    @classmethod
    def create_tracking(cls, data) -> Tracking:
        '''
        create tracking function
        '''
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
        '''
        get tracking by id
        '''
        return Tracking.objects.prefetch_related('product').get(id=id)

    @classmethod
    def get_all_tracking(cls):
        '''
        get all tracking models
        '''
        return Tracking.objects.prefetch_related('product').all()

    @classmethod
    def filter_tracking_queryset_by_text(cls, queryset, search_term):
        '''
        search queryset by text for tracking models
        '''
        if search_term:
            queryset = queryset.filter(
                product__name__icontains=search_term
            )
        return queryset

    @classmethod
    def filter_tracking_queryset_by_product_id(cls, queryset, id):
        if id:
            queryset = queryset.filter(
                product__id=id
            )
        return queryset

    @classmethod
    def filter_tracking_queryset_by_date(cls, queryset, date_string, timezone):
        '''
        timezone filtering based on timezone
        '''
        try:
            if timezone:
                d = datetime.datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%fZ')
                aware_date = pytz.timezone(timezone).localize(d)
                date_time = aware_date.astimezone(pytz.timezone('UTC'))
                end_date_time = date_time + datetime.timedelta(hours=23, minutes=59)
                if date_time and end_date_time:
                    queryset = queryset.filter(
                        timestamp__gte=date_time, timestamp__lte=end_date_time
                    )
        except Exception as exc:
            pass
        return queryset



    @classmethod
    def edit_tracking(cls, id, data):
        '''
        edit tracking models
        '''
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
        '''
        edit product object
        '''
        p = cls.get_product_by_id(id)
        p.name = data.get('name')
        p.save()
        return p
