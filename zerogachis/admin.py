from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from . import models


admin.site.register(models.ZerogachisSpot, LeafletGeoAdmin)