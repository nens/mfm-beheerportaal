
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

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
        Retrieve all measurements in a certain timerange for given devices
        """
        return Response('Not implemented')

    @action(methods=['get'], detail=True, url_path='(?P<wns_id>[^/.]+)', url_name='WNS')
    def retrieve_wns(self, request, pk, wns_id):
        """
        Retrieve a specific measurement in a certain timerange for given devices
        """
        return Response('Not implemented')
