from rest_framework import serializers

from mfm_beheerportaal import models

class MultiflexmeterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Multiflexmeter
        fields = ('identifier', 'description', 'owner',
                  'version', 'created', 'active')

class MultiflexmeterVersionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MultiflexmeterVersion
        fields = ('name', 'description', 'version_major', 'version_minor', 'version_patch')

class GatewaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Gateway
        fields = ('identifier', 'owner', 'description', 'router', 'brand')

class OrganisationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Organisation
        fields = ('name', 'abbreviation')
