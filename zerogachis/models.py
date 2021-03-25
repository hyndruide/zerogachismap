from djgeojson.fields import PointField
from django.db import models

class ZerogachisSpot(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(default = "magazin")
    picture = models.TextField()
    geom = PointField()
    partenaire = models.BooleanField()

    def __str__(self):
        return self.title + ' ' + str(self.partenaire)

