import logging

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from mfm_beheerportaal.api.v1.influxwrapper import InfluxWrapper
from mfm_beheerportaal.api.v1.models import Multiflexmeter

logger = logging.getLogger(__name__)

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
        # Ensure start and end parameters are given
        start, end = self.get_timerange(request)
        # Get resolution parameter
        resolution = request.GET.get('resolution', '1h')
        # Get devices
        mfm = Multiflexmeter.objects.get(pk=pk)
        logger.info('Retrieving timeseries')
        # Create connection
        influx = InfluxWrapper()
        # Retrieve timeseries
        result = influx.get_timeseries(mfm, 'wns8819', start, end, resolution)
        return Response(list(result.get_points()))

    @action(methods=['get'], detail=True, url_path='(?P<wns_id>[^/.]+)', url_name='WNS')
    def retrieve_wns(self, request, pk, wns_id):
        """
        Retrieve a specific measurement in a certain timerange for given devices
        """
        start, end = self.get_timerange(request)
        return Response('Not implemented')

    def get_timerange(self, request):
        """
        Return the timerange denoted by `start` and `end` parameter
        or throw if they don't exist.
        """
        start = request.GET.get('start', None)
        end = request.GET.get('end', None)
        if start is None:
            raise KeyError('start time not present in request')
        if end is None:
            raise KeyError('end time not present in request')
        return start, end

class NoTimerangeError(Exception):
    def __init__(self):
        super().__init__('Invalid timerange supplied')
