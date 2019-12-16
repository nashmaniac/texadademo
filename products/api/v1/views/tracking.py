from rest_framework.views import APIView
from core.utils import CoreResponse
from ..serializers import TrackingCreateSerializer


class TrackingApiView(APIView):
    def _get_create_serializer_class(self):
        return TrackingCreateSerializer

    def post(self, request):
        try:
            # get the serializer class
            serializer_class = self._get_create_serializer_class()
            # instantiate class
            serializer = serializer_class(data=request.data)
            # marshalling the data
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            return CoreResponse.send(data, 200)
        except Exception as exc:
            return CoreResponse.send(dict(
                status=500,
                message=str(exc)
            ), 500)
