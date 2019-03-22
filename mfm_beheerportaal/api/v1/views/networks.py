
from rest_framework import viewsets

from mfm_beheerportaal.api.v1.models import Network
from mfm_beheerportaal.api.v1.serializers import NetworkSerializer

class NetworkViewSet(viewsets.ModelViewSet):
    """API endpoint that allows networks to be viewed"""
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
