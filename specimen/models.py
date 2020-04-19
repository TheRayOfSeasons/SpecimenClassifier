import datetime
import decimal

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Specimen(models.Model):
    name = models.CharField(max_length=256, blank=True, default='')
    code = models.CharField(max_length=128, blank=True, default='')
    host_tree = models.ForeignKey('trees.Tree', on_delete=models.CASCADE)
    location = models.ForeignKey('locations.Location', on_delete=models.CASCADE)
    latitude = models.CharField(max_length=256, blank=True, default='')
    longhitude = models.CharField(max_length=256, blank=True, default='')
    dbh = models.DecimalField(
        max_digits=19,
        decimal_places=2
    )
    collection_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.name} - {self.code}'

    @property
    def get_distinct_organisms(self):
        north = self.northorganism_set.all()
        east = self.eastorganism_set.all()
        west = self.westorganism_set.all()
        south = self.southorganism_set.all()

        distinct_organisms = []

        for collection in [north, east, west, south]:
            for item in collection:
                organism = item.epiphytic_organism
                if organism.name not in distinct_organisms:
                    distinct_organisms.append(organism.name)

        return distinct_organisms
