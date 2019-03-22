from django.db import models
from django.utils.translation import ugettext_lazy as _

import datetime

# Create your models here.


class Organisation(models.Model):
    """An organisation"""
    full_name = models.CharField(
        max_length=100)
    short_name = models.CharField(
        max_length=100,
        blank=True)


class MultiflexmeterVersion(models.Model):
    """Specifies a Multiflexmeter version"""
    full_name = models.CharField(
        max_length=100)
    short_name = models.CharField(
        max_length=100)


class PhysicalLocationMixin(models.Model):
    """Defines a physical location through coordinates with altitude.
    Defaults to (0,0,0)"""
    # Location
    latitude = models.DecimalField(
        _('Latitude'),
        default=0,
        max_digits=11,
        decimal_places=8)
    longitude = models.DecimalField(
        _('Longitude'),
        default=0,
        max_digits=11,
        decimal_places=8)
    altitude = models.DecimalField(
        _('Altitude'),
        default=0,
        max_digits=11,
        decimal_places=8)


class Multiflexmeter(PhysicalLocationMixin, models.Model):
    """A Multiflexmeter device"""
    identifier = models.CharField(
        _('Identifier'),
        max_length=100,
        unique=True)
    description = models.TextField(
        _('Description'),
        max_length=100)
    owner = models.ForeignKey(
        Organisation,
        on_delete=models.SET_NULL,
        null=True)
    version = models.ForeignKey(
        MultiflexmeterVersion,
        on_delete=models.SET_NULL,
        null=True)
    created = models.DateField(
        _('Created on'),
        default=datetime.date.today)
    active = models.BooleanField(
        _('Active'),
        default=False)

        MultiflexmeterVersion, on_delete=models.SET_NULL, null=True)
    created = models.DateField(_('Created on'), default=datetime.date.today)
    active = models.BooleanField(_('Active'), default=False)


class Gateway(PhysicalLocationMixin, models.Model):
    """A physical LoRa gateway"""
    identifier = models.CharField(
        _('Identifier'),
        max_length=100,
        unique=True)
    owner = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE)
    description = models.TextField(
        _('Description'))
    router = models.CharField(
        max_length=100)
    brand = models.CharField(
        max_length=100)
