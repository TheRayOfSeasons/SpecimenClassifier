from django.db import models
from django.utils.translation import gettext_lazy as _

from epiphytes.models import EpiphyticOrganism
from specimen.models import Specimen


class Directions(models.TextChoices):
    NORTH = 'N', _('North')
    EAST = 'E', _('East')
    WEST = 'W', _('West')
    SOUTH = 'S', _('South')


class DirectionSampleDetailsModel(models.Model):
    specimen = models.OneToOneField(Specimen, on_delete=models.CASCADE)
    ph_level = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        null=True,
        blank=True,
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


class DirectionOrganism(models.Model):
    specimen = models.ForeignKey(Specimen, on_delete=models.CASCADE)
    epiphytic_organism = models.ForeignKey(EpiphyticOrganism, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class NorthOrganism(DirectionOrganism):
    def __str__(self):
        return f'{self.specimen.name}'


class WestOrganism(DirectionOrganism):
    def __str__(self):
        return f'{self.specimen.name}'


class EastOrganism(DirectionOrganism):
    def __str__(self):
        return f'{self.specimen.name}'


class SouthOrganism(DirectionOrganism):
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
