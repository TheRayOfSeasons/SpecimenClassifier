import datetime
import decimal

from django.db import models
from django.utils import timezone
from trees.models import Tree
from django.utils.translation import gettext_lazy as _


class Directions(models.TextChoices):
    NORTH = 'N', _('North')
    EAST = 'E', _('East')
    WEST = 'W', _('West')
    SOUTH = 'S', _('South')


class StateOfDecay(models.TextChoices):
    INTACT = 'i', _('intact')
    MODERATELY_INTACT = 'mi', _('moderately intact')
    LOOSE = 'l', _('loose')


class Texture(models.TextChoices):
    SMOOTH = 's', _('smooth')
    ROUGH = 'r', _('rough')


class Location(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Specimen(models.Model):
    name = models.CharField(max_length=256, blank=True, default='<Blank>')
    code = models.CharField(max_length=128, blank=True, default='<Blank>')
    host_tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=256, blank=True, default='Not Specified')
    longhitude = models.CharField(max_length=256, blank=True, default='Not Specified')
    dbh = models.DecimalField(
        max_digits=19,
        decimal_places=2
    )
    collection_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.name} - {self.code}'


# class Direction(models.Model):
#     specimen = models.ForeignKey(Specimen, on_delete=models.CASCADE)
#     name = models.CharField(
#         max_length=8,
#         choices=Directions.choices,
#         default=Directions.NORTH
#     )

#     def __str__(self):
#         return f'{self.name} | {self.specimen.name} | {self.specimen.code}'

    # @property
    # def average(self):
    #     samples = sample_set.select_related('score')
    #     avg = decimal.Decimal(0)

    #     for sample in samples:
    #         avg += sample.score

    #     avg /= len(samples)

    #     return avg


class SpecimenDetails(models.Model):
    specimen = models.ForeignKey(Specimen, on_delete=models.CASCADE)
    direction = models.CharField(
        max_length=8,
        choices=Directions.choices,
        default=Directions.NORTH
    )
    state_of_decay = models.CharField(
        max_length=8,
        choices=StateOfDecay.choices,
        default=StateOfDecay.INTACT
    ),
    bark_texture = models.CharField(
        max_length=8,
        choices=Texture.choices,
        default=Texture.SMOOTH
    )
    stain = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.specimen.name} - {self.specimen.code}'


class EpyphyticOrganism(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class SpecimenEpyphyticOrganism(models.Model):
    specimen = models.ForeignKey(Specimen, on_delete=models.CASCADE)
    direction = models.CharField(
        max_length=8,
        choices=Directions.choices,
        default=Directions.NORTH
    )
    organism = models.ForeignKey(EpyphyticOrganism, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.direction.specimen.name} | {self.organism.name}'


class Sample(models.Model):
    specimen = models.ForeignKey(Specimen, on_delete=models.CASCADE)
    direction = models.CharField(
        max_length=8,
        choices=Directions.choices,
        default=Directions.NORTH
    )
    ph_level = models.DecimalField(
        max_digits=19,
        decimal_places=2
    )
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'{self.specimen.name} - {self.specimen.code}'
