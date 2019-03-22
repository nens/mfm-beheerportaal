from django.utils.translation import ugettext as _
# from django.core.urlresolvers import reverse
from rest_framework import viewsets

from mfm_beheerportaal.models import Organisation
from mfm_beheerportaal.serializers import OrganisationSerializer

class OrganisationViewSet(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer