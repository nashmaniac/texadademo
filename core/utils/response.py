from rest_framework import status
from rest_framework.response import Response


class CoreResponse(object):
    status_matcher = {
        500: status.HTTP_500_INTERNAL_SERVER_ERROR,
        403: status.HTTP_403_FORBIDDEN,
        400: status.HTTP_400_BAD_REQUEST,
        200: status.HTTP_200_OK,
        404: status.HTTP_404_NOT_FOUND
    }

    @classmethod
    def send(cls, payload, status_code):
        return Response(payload, status=cls.status_matcher[status_code])
