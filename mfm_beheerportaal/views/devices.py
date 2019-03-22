from django.utils.translation import ugettext as _
# from django.core.urlresolvers import reverse
from rest_framework import viewsets

from mfm_beheerportaal.models import Multiflexmeter
from mfm_beheerportaal import serializers

class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows devices to be viewed or edited.
    """
    queryset = Multiflexmeter.objects.all()
    serializer_class = serializers.MultiflexmeterSerializer
