from django.utils.translation import ugettext as _
# from django.core.urlresolvers import reverse
from rest_framework import viewsets

from mfm_beheerportaal.api.v1.models import Organisation
from mfm_beheerportaal.api.v1.serializers import OrganisationSerializer

class OrganisationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows organisations to be viewed or edited.
    """
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
