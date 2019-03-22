import datetime

from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from mfm_beheerportaal import validators

# Create your models here.


class Organisation(Group):
    """An organisation as group"""
    abbreviation = models.CharField(
        primary_key=True,
        max_length=100,
        unique=True,
        blank=True
    )


class Network(models.Model):
    """A network which provides communication"""
    abbreviation = models.CharField(
        _('Abbreviation'),
        primary_key=True,
        max_length=100,
        unique=True
    )
    name = models.CharField(
        _('Name'),
        max_length=100,
        unique=True
    )
    active = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.name

class MultiflexmeterVersion(models.Model):
    """Specifies a Multiflexmeter version"""
    name = models.CharField(
        max_length=100,
        unique=True,
        primary_key=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    version_major = models.IntegerField(
        _("Major version")
    )
    version_minor = models.IntegerField(
        _("Minor version")
    )
    version_patch = models.IntegerField(
        _("Patch version")
    )

    def get_version(self):
        """Get the semantic version as string"""
        return f'{self.version_major}.{self.version_minor}.{self.version_patch}'

    def __str__(self):
        return f'{self.name} {self.get_version()}'


class PhysicalLocationMixin(models.Model):
    """
    Defines a physical location through coordinates with altitude.
    Defaults to (0,0,0).
    """
    # Location
    latitude = models.DecimalField(
        _('Latitude'),
        default=0,
        max_digits=11,
        decimal_places=8
    )
    longitude = models.DecimalField(
        _('Longitude'),
        default=0,
        max_digits=11,
        decimal_places=8
    )
    altitude = models.DecimalField(
        _('Altitude'),
        default=0,
        max_digits=11,
        decimal_places=8
    )

    class Meta:
        abstract = True


class Multiflexmeter(PhysicalLocationMixin, models.Model):
    """A Multiflexmeter device"""
    identifier = models.CharField(
        _('Identifier'),
        primary_key=True,
        max_length=100,
        unique=True
    )
    description = models.TextField(
        _('Description'),
        max_length=100,
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        Organisation,
        on_delete=models.SET_NULL,
        null=True
    )
    network = models.ForeignKey(
        Network,
        on_delete=models.SET_NULL,
        null=True
    )
    version = models.ForeignKey(
        MultiflexmeterVersion,
        on_delete=models.SET_NULL,
        null=True
    )
    created = models.DateField(
        _('Created on'),
        default=datetime.date.today
    )
    active = models.BooleanField(
        _('Active'),
        default=False
    )

    def __str__(self):
        return self.identifier

class WNS(models.Model):
    """A dutch specification for measurement properties"""
    number = models.CharField(
        primary_key=True,
        max_length=100,
        unique=True
    )
    name = models.CharField(
        max_length=100,
        unique=True
    )
    unit = models.CharField(
        max_length=100
    )
    format = models.CharField(
        max_length=100
    )
    
    def __str__(self):
        return self.name


class Gateway(PhysicalLocationMixin, models.Model):
    """A physical LoRa gateway"""
    identifier = models.CharField(
        _('Identifier'),
        primary_key=True,
        max_length=100,
        unique=True
    )
    owner = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE
    )
    description = models.TextField(
        _('Description'),
        blank=True,
        null=True
    )
    router = models.CharField(
        max_length=100
    )
    brand = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.identifier

