
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from mfm_beheerportaal.api.v1 import views

router = routers.DefaultRouter()
router.register(r'devices', views.devices.DeviceViewSet)
router.register(r'device-versions', views.device_version.DeviceVersionViewSet)
router.register(r'gateways', views.gateways.GatewayViewSet)
router.register(r'organisations', views.organisations.OrganisationViewSet)
router.register(r'timeseries', views.TimeserieViewSet, basename='timeseries')

urlpatterns = [
    path('', include(router.urls))
]
