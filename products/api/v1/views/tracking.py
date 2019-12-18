from rest_framework.views import APIView
from core.utils import CoreResponse, CoreUtils
from ..serializers import TrackingCreateSerializer, TrackSerializer
from products.datalayers import ProductDataLayer


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
            # create tracking
            t = ProductDataLayer.create_tracking(serializer.validated_data)
            # serializing data
            data = TrackSerializer(t).data
            return CoreResponse.send(data, 200)
        except Exception as exc:
            return CoreResponse.send(dict(
                status=500,
                message=str(exc)
            ), 500)

    def get(self, request):
        try:
            page_size = int(request.query_params.get('pageSize', CoreUtils.get_default_page_size()))
            page_index = int(request.query_params.get('pageIndex', CoreUtils.get_default_page_index()))
            search_term = request.query_params.get('searchTerm', None)
            current_sort = request.query_params.get('currentSort', None)
            current_sort_dir = request.query_params.get('currentSortDir', None)
            selected_product = request.query_params.get('selectedProduct', None)
            selected_date = request.query_params.get('selectedDate', None)
            timezone = request.query_params.get('timezone', None)
            print(selected_date)
            start, end, page, limit = CoreUtils.get_start_end_index(page_index, page_size)
            t = ProductDataLayer.get_all_tracking()
            t = ProductDataLayer.filter_tracking_queryset_by_text(t, search_term)
            t = ProductDataLayer.filter_tracking_queryset_by_product_id(t, selected_product)
            t = ProductDataLayer.filter_tracking_queryset_by_date(t, selected_date, timezone)
            if current_sort and current_sort_dir:
                sorting_params = '-%s'%current_sort if current_sort_dir == 'desc' else '%s'%current_sort
                t = t.order_by(sorting_params)
            t = t.distinct()
            count = t.count()
            data = dict(
                page=page,
                limit=limit,
                count=count,
                data=TrackSerializer(t[start:end], many=True).data
            )
            return CoreResponse.send(data, 200)
        except Exception as exc:
            return CoreResponse.send(
                dict(status=500, message=str(exc)), 500
            )


class TrackingDetailApiView(APIView):
    def _get_edit_serializer_class(self):
        return TrackingCreateSerializer

    def put(self, request, id):
        try:
            serializer_class = self._get_edit_serializer_class()
            serializer = serializer_class(data=request.data);
            serializer.is_valid(raise_exception=True)
            t = ProductDataLayer.edit_tracking(id, serializer.validated_data)
            data = TrackSerializer(t).data
            return CoreResponse.send(data, 200)
        except Exception as exc:
            return CoreResponse.send(
                dict(
                    status=500,
                    message=str(exc)
                ), 500
            )

    def get(self, request, id):
        try:
            t = ProductDataLayer.get_tracking_by_id(id)
            data = TrackSerializer(t).data
            return CoreResponse.send(data, 200)
        except Exception as exc:
            return CoreResponse.send(
                dict(
                    status=500,
                    message=str(exc)
                ), 500
            )

    def delete(self, request, id):
        try:
            t = ProductDataLayer.get_tracking_by_id(id)
            t.delete(soft=False)
            return CoreResponse.send(dict(), 200)
        except Exception as exc:
            return CoreResponse.send(
                dict(
                    status=500,
                    message=str(exc)
                ), 500
            )