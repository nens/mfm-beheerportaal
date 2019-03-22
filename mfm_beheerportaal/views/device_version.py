from django.utils.translation import ugettext as _
# from django.core.urlresolvers import reverse
from rest_framework import viewsets

from mfm_beheerportaal.models import MultiflexmeterVersion
from mfm_beheerportaal import serializers

class DeviceVersionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows device versions to be viewed or edited.
    """
    queryset = MultiflexmeterVersion.objects.all()
    serializer_class = serializers.MultiflexmeterVersionSerializer
