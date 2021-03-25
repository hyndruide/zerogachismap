from djgeojson.views import GeoJSONLayerView
from .models import ZerogachisSpot

class MapPartenaire(GeoJSONLayerView):
    # Options
    precision = 4   # float
    simplify = 0.5  # generalization

    def get_queryset(self):
        return ZerogachisSpot.objects.filter(partenaire = True)

class MapNonPartenaire(GeoJSONLayerView):
    # Options
    precision = 4   # float
    simplify = 0.5  # generalization

    def get_queryset(self):
        return ZerogachisSpot.objects.filter(partenaire = False)