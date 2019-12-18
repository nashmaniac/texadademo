from rest_framework.views import APIView
from core.utils import CoreResponse, CoreUtils
from products.datalayers import ProductDataLayer
from ..serializers import ProductCreateSerializer, ProductSerializer


class ProductApiView(APIView):
    def _get_create_serializer_class(self):
        return ProductCreateSerializer

    def get(self, request):
        try:
            page_size = int(request.query_params.get('pageSize', CoreUtils.get_default_page_size()))
            page_index = int(request.query_params.get('pageIndex', CoreUtils.get_default_page_index()))
            search_term = request.query_params.get('searchTerm', None)
            current_sort = request.query_params.get('currentSort', None)
            current_sort_dir = request.query_params.get('currentSortDir', None)
            start, end, page, limit = CoreUtils.get_start_end_index(page_index, page_size)
            p = ProductDataLayer.get_all_products()
            p = ProductDataLayer.filter_product_queryset_by_text(p, search_term)
            if current_sort and current_sort_dir:
                sorting_params = '-%s'%current_sort if current_sort_dir == 'desc' else '%s'%current_sort
                p = p.order_by(sorting_params)
            p = p.distinct()
            count = p.count()
            data = dict(
                page=page,
                limit=limit,
                count=count,
                data=ProductSerializer(p[start:end], many=True).data
            )
            return CoreResponse.send(data, 200)
        except Exception as exc:
            return CoreResponse.send(dict(
                status=500,
                message=str(exc)
            ), 500)

    def post(self, request):
        try:
            # getting serializer class
            serializer_class = self._get_create_serializer_class()
            # instantiate serializer class
            serializer = serializer_class(data=request.data)
            # checking the validity
            serializer.is_valid(raise_exception=True)
            # using data abstraction layer to create object
            p = ProductDataLayer.create_product(**serializer.validated_data)
            # convert object to database
            data = ProductSerializer(p).data
            # send the data to response
            return CoreResponse.send(data, 200)
        except Exception as exc:
            return CoreResponse.send(dict(
                status=500,
                message=str(exc)
            ), 500)


class ProductDetailApiView(APIView):
    def _get_edit_serializer_class(self):
        return ProductCreateSerializer

    def put(self, request, id):
        try:
            serializer_class = self._get_edit_serializer_class()
            serializer = serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            p = ProductDataLayer.edit_product(id, serializer.validated_data)
            data = ProductSerializer(p).data
            return CoreResponse.send(data, 200)
        except Exception as exc:
            return CoreResponse.send(dict(
                status=500,
                messsage=str(exc)
            ), 500)

    def get(self, request, id):
        try:
            # get the product by id
            p = ProductDataLayer.get_product_by_id(id)
            # serialize the object
            data = ProductSerializer(p).data
            return CoreResponse.send(data, 200)
        except Exception as exc:
            return CoreResponse.send(dict(
                status=500,
                messsage=str(exc)
            ), 500)

    def delete(self, request, id):
        try:
            # get the product by id
            p = ProductDataLayer.get_product_by_id(id)
            p.delete(soft=False)
            data = dict()
            return CoreResponse.send(data, 200)
        except Exception as exc:
            return CoreResponse.send(dict(
                status=500,
                messsage=str(exc)
            ), 500)

