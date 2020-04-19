from statistics import mean

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.files.storage import FileSystemStorage

from epiphytes.models import EpiphyticOrganism
from specimen.models import Specimen


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


class DirectionSampleDetailsModel(models.Model):
    specimen = models.OneToOneField(Specimen, on_delete=models.CASCADE)
    ph_level_1 = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        null=True,
        blank=True,
    )
    ph_level_2 = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        null=True,
        blank=True,
    )
    ph_level_3 = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        null=True,
        blank=True,
    )
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

    class Meta:
        abstract = True

    @property
    def average_ph(self):
        ph_list = []
        for ph in [
                    self.ph_level_1,
                    self.ph_level_2,
                    self.ph_level_3
                ]:
            if ph:
                ph_list.append(ph)
        return round(mean(ph_list), 2)


class NorthDetails(DirectionSampleDetailsModel):
    def __str__(self):
        return f'{self.specimen.name}'


class EastDetails(DirectionSampleDetailsModel):
    def __str__(self):
        return f'{self.specimen.name}'


class WestDetails(DirectionSampleDetailsModel):
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
        return f'{self.epiphytic_organism.name}'


class EastOrganism(DirectionOrganism):
    def __str__(self):
        return f'{self.epiphytic_organism.name}'


class WestOrganism(DirectionOrganism):
    def __str__(self):
        return f'{self.epiphytic_organism.name}'


class SouthOrganism(DirectionOrganism):
    def __str__(self):
        return f'{self.epiphytic_organism.name}'


class DirectionImagesModel(models.Model):
    specimen = models.ForeignKey(Specimen, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class NorthImages(DirectionImagesModel):
    image = models.ImageField(blank=True, null=True,
        upload_to='specimen_images/north/')

    def __str__(self):
        return f'{self.specimen.name} | {self.image}'


class EastImages(DirectionImagesModel):
    image = models.ImageField(blank=True, null=True,
        upload_to='specimen_images/east/')

    def __str__(self):
        return f'{self.specimen.name} | {self.image}'


class WestImages(DirectionImagesModel):
    image = models.ImageField(blank=True, null=True,
        upload_to='specimen_images/west/',
        storage=FileSystemStorage())

    def __str__(self):
        return f'{specimen.name} | {self.image}'


class SouthImages(DirectionImagesModel):
    image = models.ImageField(blank=True, null=True,
        upload_to='specimen_images/south/')

    def __str__(self):
        return f'{self.specimen.name} | {self.image}'
