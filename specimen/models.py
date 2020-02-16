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
    INTACT = 'i', _('Intact')
    MODERATELY_INTACT = 'mi', _('Moderately Intact')
    LOOSE = 'l', _('Loose')


class Texture(models.TextChoices):
    SMOOTH = 's', _('Smooth')
    ROUGH = 'r', _('Rough')


class Location(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Specimen(models.Model):
    name = models.CharField(max_length=256, blank=True, default='')
    code = models.CharField(max_length=128, blank=True, default='')
    host_tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=256, blank=True, default='')
    longhitude = models.CharField(max_length=256, blank=True, default='')
    dbh = models.DecimalField(
        max_digits=19,
        decimal_places=2
    )
    collection_date = models.DateField(default=timezone.now)
    state_of_decay = models.CharField(
        max_length=8,
        choices=StateOfDecay.choices,
        default=StateOfDecay.INTACT
    )
    bark_texture = models.CharField(
        max_length=8,
        choices=Texture.choices,
        default=Texture.SMOOTH
    )
    stain = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.code}'


class EpyphyticOrganism(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class SpecimenEpyphyticOrganism(models.Model):
    specimen = models.ForeignKey(Specimen, on_delete=models.CASCADE)
    organism = models.ForeignKey(EpyphyticOrganism, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.direction.specimen.name} | {self.organism.name}'


class DirectionSampleDetailsModel(models.Model):
    specimen = models.OneToOneField(Specimen, on_delete=models.CASCADE)
    ph_level = models.DecimalField(
        max_digits=19,
        decimal_places=2
    )

    class Meta:
        abstract = True


class NorthDetails(DirectionSampleDetailsModel):
    def __str__(self):
        return f'{self.specimen.name}'


class WestDetails(DirectionSampleDetailsModel):
    def __str__(self):
        return f'{self.specimen.name}'


class EastDetails(DirectionSampleDetailsModel):
    def __str__(self):
        return f'{self.specimen.name}'


class SouthDetails(DirectionSampleDetailsModel):
    def __str__(self):
        return f'{self.specimen.name}'


class DirectionImagesModel(models.Model):
    specimen = models.ForeignKey(Specimen, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)

    class Meta:
        abstract = True


class NorthImages(DirectionImagesModel):

    def __str__(self):
        return f'{self.details.specimen.name}'


class EastImages(DirectionImagesModel):

    def __str__(self):
        return f'{self.details.specimen.name}'


class WestImages(DirectionImagesModel):

    def __str__(self):
        return f'{self.details.specimen.name}'


class SouthImages(DirectionImagesModel):

    def __str__(self):
        return f'{self.details.specimen.name}'
