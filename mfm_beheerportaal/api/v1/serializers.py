from rest_framework import serializers

from mfm_beheerportaal.api.v1 import models

class MultiflexmeterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Multiflexmeter
        fields = ('identifier', 'description', 'owner',
                  'network', 'version', 'created', 'active')

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

class NetworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Network
        fields = ('name', 'active')