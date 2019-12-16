from rest_framework.views import APIView
from core.utils import CoreResponse
from products.datalayers import ProductDataLayer
from ..serializers import ProductCreateSerializer, ProductSerializer


class ProductApiView(APIView):
    def _get_create_serializer_class(self):
        return ProductCreateSerializer

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
    def get(self, request, id):
        try:
            p = ProductDataLayer.get_product_by_id(int(id))
            data = ProductSerializer(p).data
            return CoreResponse.send(data, 200)
        except Exception as exc:
            return CoreResponse.send(dict(
                status=500,
                messsage=str(exc)
            ), 500)