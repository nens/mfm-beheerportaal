from django.utils.translation import ugettext as _
# from django.core.urlresolvers import reverse
from rest_framework import viewsets

from mfm_beheerportaal.models import Gateway
from mfm_beheerportaal.serializers import GatewaySerializer

class GatewayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows gateways to be viewed or edited.
    """
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer