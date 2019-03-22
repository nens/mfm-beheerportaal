
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

class TimeserieViewSet(ViewSet):
    """
    API endpoint that allows timeseries and metadata to be viewed.
    """
    def list(self, request):
        """
        List metadata for all timeseries you have read access to.
        """
        return Response('Not implemented')

    def retrieve(self, request, pk):
        """
        Retrieve a range of data from a timeseries.
        """
        return Response('Not implemented')
