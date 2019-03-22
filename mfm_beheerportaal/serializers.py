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
        fields = ('full_name', 'short_name')
